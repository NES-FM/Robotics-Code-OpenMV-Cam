import pyb
import sensor, time, tf, math, gc, omv
import uos
import image
from image import Image
from lib import lib_ard, lib_objects
from pyb import USB_VCP, LED
from lib.lib_objects import constrain

from lib.vl53l5cx import RANGING_MODE_AUTONOMOUS, RANGING_MODE_CONTINUOUS, POWER_MODE_SLEEP, POWER_MODE_WAKEUP
from lib.vl53l5cx import TARGET_ORDER_CLOSEST, TARGET_ORDER_STRONGEST, RESOLUTION_4X4, RESOLUTION_8X8
from lib.vl53l5cx import DATA_AMBIENT_PER_SPAD, DATA_NB_SPADS_ENABLED, DATA_NB_TARGET_DETECTED, DATA_SIGNAL_PER_SPAD, DATA_RANGE_SIGMA_MM, DATA_DISTANCE_MM, DATA_REFLECTANCE, DATA_TARGET_STATUS, DATA_MOTION_INDICATOR
from lib.vl53l5cx import STATUS_VALID
from lib.vl53l5cx import VL53L5CXMP, make_sensor, map_index_to_y_pos

### CONFIG
DEBUG_IN_IDE = True
MIN_TF_CONF = 0.4 # Min Config for TensorFlow Detection
CIRCLE_THRESH = 1700 # Detection Threshold for circle detection
X_OFFSET_WINDOWING = 70  # Range: 0-80

CORNER_ENABLED = True
BALLS_ENABLED = True
EXIT_LINE_ENABLED = False
TOF_ENABLED = True
### ENDCONFIG

### GLOBAL VARIABLES
# default IDs
background_id = 0
exit_line_id = 10
silver_ball_id = 11
black_ball_id = 12
corner_id = 13

colors = []

black_white = True
net: tf.tf_model
labels = None

balls: list[lib_objects.ball] = []
corner = lib_objects.corner().init(reset=True)
exit_line = lib_objects.exit_line().init(reset=True)
ard_comm = lib_ard.ard_comm_uart()
img: Image

OMV_DEBUG = False
usb = USB_VCP()

tof: VL53L5CXMP
tof_detection_results = Image(8, 8, sensor.GRAYSCALE)
tof_detection_results_240 = Image(240, 240, sensor.GRAYSCALE)
### ENDGLOBAL

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def do_boxes_overlap(box1, box2):
    x1 = box1[0]
    y1 = box1[1]
    x2 = x1 + box1[2]
    y2 = y1 + box1[3]

    x3 = box2[0]
    y3 = box2[1]
    x4 = x3 + box2[2]
    y4 = y3 + box2[3]

    return (x1 < x4) and (x2 > x3) and (y1 < y4) and (y2 > y3)

def init_tof():
    global TOF_ENABLED, tof
    if TOF_ENABLED:
        tof = make_sensor()
        tof.reset()

        TOF_ENABLED = tof.is_alive()

        tof.init()

        tof.resolution = RESOLUTION_8X8
        tof.ranging_freq = 10
        tof.ranging_mode = RANGING_MODE_AUTONOMOUS
        tof.target_order = TARGET_ORDER_CLOSEST


def init_sensor():
    omv.disable_fb(True)

    sensor.reset()                         # Reset and initialize the sensor.
    sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
    sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
    sensor.set_vflip(True)
    sensor.set_hmirror(True)
    sensor.set_windowing((X_OFFSET_WINDOWING, 0, 240, 240))        # Set 240x240 window.
    sensor.skip_frames(time=500)          # Let the camera adjust.

def load_tf_models():
    global net, labels, background_id, exit_line_id, silver_ball_id, black_ball_id, corner_id
    try:
        # load the model, alloc the model file on the heap if we have at least 64K free after loading
        net = tf.load("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))
    except Exception as e:
        raise Exception('Failed to load "trained.tflite"(' + str(e) + ')')

    try:
        labels = [line.rstrip('\n') for line in open("labels.txt")]

        for i, label in enumerate(labels):
            if label == "background":
                background_id = i
            elif label == "black_ball":
                black_ball_id = i
            elif label == "silver_ball":
                silver_ball_id = i
            elif label == "corner":
                corner_id = i
        print(f"IDs: backg={background_id} silver={silver_ball_id} black={black_ball_id} corner={corner_id}")
    except Exception as e:
        raise Exception('Failed to load "labels.txt"(' + str(e) + ')')

def init_colors():
    global colors
    for i in range(0, 15):
        if i == black_ball_id:
            colors.append((255, 0,   0  ))
        elif i == exit_line_id:
            colors.append((0,   0,   255))
        elif i == silver_ball_id:
            colors.append((0,   255, 0  ))
        elif i == corner_id:
            colors.append((255, 255, 0  ))
        else:
            colors.append((0, 0, 0))

def blink_led():
    if OMV_DEBUG:
        led = LED(2)
    else:
        led = LED(1)

    led.on()
    time.sleep_ms(200)
    led.off()

def start_tof_ranging():
    global TOF_ENABLED, tof
    if TOF_ENABLED:
        tof.start_ranging({DATA_DISTANCE_MM, DATA_TARGET_STATUS})

def get_tof_results():
    global TOF_ENABLED, tof, tof_detection_results, tof_detection_results_240
    if TOF_ENABLED:
        if tof.check_data_ready():
            results = tof.get_ranging_data()
            distance = results.distance_mm
            status = results.target_status

            if not isinstance(distance, type(None)) and not isinstance(status, type(None)):
                for i, d in enumerate(distance):
                    try:
                        if status[i] == STATUS_VALID:
                            tof_detection_results.set_pixel(7-int(i/8), map_index_to_y_pos[i%8], int(distance[i]/10))
                        else:
                            tof_detection_results.set_pixel(7-int(i/8), map_index_to_y_pos[i%8], 255)
                    except Exception as e:
                        print(f"Error with TOF_value at i:{i} dis:{distance[i]}, status:{status[i]}")

                    #if (7-int(i/8)) == 0:
                        #tof_detection_results.set_pixel(7-int(i/8), map_index_to_y_pos[i%8], int(distance[i-8]/10))
                    #elif (7-int(i/8)) == 7:
                        #tof_detection_results.set_pixel(7-int(i/8), map_index_to_y_pos[i%8], int(distance[i+8]/10))
                    #else:
                        #tof_detection_results.set_pixel(7-int(i/8), map_index_to_y_pos[i%8], int((distance[i-8] + distance[i+8]) / 20))

            tof_detection_results_240.draw_image(tof_detection_results, 100, 140, x_size=280, y_size=280, hint=image.CENTER|image.BILINEAR)
            #tof_detection_results_240.gaussian(2)

            return True
    return False

def get_distance_in_roi(roi):
    return tof_detection_results_240.get_histogram(roi=roi).get_statistics().lq()

def black_white_handler():
    global balls, corner, img
    #print("before corner")
    if CORNER_ENABLED:
        corner.init(reset=True)
        temp_corner_list: list[lib_objects.corner] = []
        # Search for black blobs as corners:
        #print("before find_blobs")
        for b in img.find_blobs([(0, 40)], roi=(0, 12, 240, 200), merge=True, margin=5):
            (x, y, w, h) = b.rect()
            if h > 15:
                temp_corner_list.append( lib_objects.corner().init( screen_rect=b.rect(), histogram=img.get_histogram(roi=b.rect()), blob=b, detected_by_tf=False ) )
                distance = temp_corner_list[-1].get_distance()

                conf_by_roundness = constrain(map_range(b.roundness(), 0.02, 0.2, 1, 0), 0, 1)
                conf_by_elong = constrain(map_range(b.elongation(), 0.8, 0.99, 0, 1), 0, 1)
                conf_by_dens = constrain(map_range(b.density(), 0.4, 0.8, 0, 1), 0, 1)

                if conf_by_dens > 0.45:
                    expected_pix_count = (-165.01 * distance + 18000.0) #+ 17174.0)
                    expected_w = (-1.7528 * distance + 310.0) #+ 291.4)
                    expected_h = (-0.5139 * distance + 85.0) #+ 71.45)

                    #                                                                                                  from     to       constrain
                    conf_by_pix_count = constrain(map_range(abs(b.pixels() - expected_pix_count) / expected_pix_count, 0.25, 1, 1, 0),   0, 1)    #( 20000.0 - abs(  - b.pixels() ) ) / 20000.0
                    conf_by_w = constrain(map_range(abs(w - expected_w) / expected_w,                                  0,    1, 1, 0),   0, 1)    #( 400.0 - abs(  - w) ) / 400.0
                    conf_by_h = constrain(map_range(abs(h - expected_h) / expected_h,                                  0.1,    1, 1, 0),   0, 1)    #( 80.0 - abs(  - h) ) / 80.0

                    end_x = x + w
                    if end_x != 240 and x != 0:  # Full Rectange Visible
                        temp_corner_list[-1].confidence = (0.13 * conf_by_roundness) + (0.13 * conf_by_elong) + (0.20 * conf_by_dens) + (0.2 * conf_by_pix_count) + (0.14 * conf_by_w) + (0.2 * conf_by_h)
                    else:
                        temp_corner_list[-1].confidence = (0 * conf_by_roundness) + (0 * conf_by_elong) + (0.3 * conf_by_dens) + (0.3 * conf_by_pix_count) + (0.15 * conf_by_w) + (0.25 * conf_by_h)

                    print(f"Possible corner: x{x} y{y} w{w} h{h} x_off{temp_corner_list[-1].get_x_offset()} "
                    + f"dist{temp_corner_list[-1].get_distance()} pix{b.pixels()} rot{b.rotation_deg()}° round{b.roundness()} "
                    + f"elong{b.elongation()} dens{b.density()} convex{b.convexity()} "
                    + f"conf{temp_corner_list[-1].confidence} = [round:{conf_by_roundness}, elong:{conf_by_elong}, dens:{conf_by_dens}, pix:{conf_by_pix_count}, w:{conf_by_w}, h:{conf_by_h}]")
                else:
                    print(f"Corner x{x} y{y} w{w} h{h} Dismissed because conf_by_dens{conf_by_dens} < 0.45")
            else:
                print(f"Corner x{x} y{y} w{w} h{h} Dismissed because h{h} <= 15")

        # Only keep highest confidence corner
        if len(temp_corner_list) > 0:
            possible_corner = max(temp_corner_list, key=lambda x: x.confidence)
            if possible_corner.confidence > 0.7:
                corner = possible_corner
                x, y, w, h = corner.get_screen_rect()
                b = corner.blob
                print(f"Selceted corner: x{x} y{y} w{w} h{h} x_off{corner.get_x_offset()} dist{corner.get_distance()} conf{corner.confidence} pix{b.pixels()} rot{b.rotation_deg()}° round{b.roundness()} elong{b.elongation()} dens{b.density()} convex{b.convexity()}")

    #print("before balls")
    if BALLS_ENABLED:
        balls.clear()
        # Tensorflow detection
        for i, detection_list in enumerate(net.detect(img, thresholds=[(math.ceil(MIN_TF_CONF * 255), 255)])):
            if (i == 0): continue # background class
            if (len(detection_list) == 0): continue # no detections for this class?

            for d in detection_list:
                if not do_boxes_overlap(d.rect(), (0, 208, 190, 33)) and not do_boxes_overlap(d.rect(), (0, 170, 130, 70)):  # Make sure that claw doesn't get detected
                    if i == black_ball_id:  # black ball
                        balls.append( lib_objects.ball().init( screen_rect=d.rect(), classified_as=lib_objects.ball.BLACK, classification_value=d.output(), histogram=img.get_histogram(roi=d.rect()) ) )
                    elif i == silver_ball_id:  # silver_ball
                        balls.append( lib_objects.ball().init( screen_rect=d.rect(), classified_as=lib_objects.ball.SILVER, classification_value=d.output(), histogram=img.get_histogram(roi=d.rect()) ) )
                    # elif i == corner_id:  # corner
                    #     temp_corner_list.append( lib_objects.corner().init( screen_rect=d.rect(), classification_value=d.output(), histogram=img.get_histogram(roi=d.rect()), detected_by_tf=True ) )

        img.gaussian(1)
        # For every ball found, search for circles within the area
        for ball in balls:
            x, y, w, h = ball.get_screen_rect()
            circle_det_rad = constrain(int(map_range(ball.get_distance(), 11, 60, 50, 15)), 0, 240)
            circle_min_rad = constrain(int(map_range(ball.get_distance(), 11, 60, 20, 4)), 0, 240)
            sx, sy, sw, sh = x-circle_det_rad, y-circle_det_rad, w+2*circle_det_rad, h+2*circle_det_rad
            ball.set_screen_det_rad(sx, sy, sw, sh)
            try:
                for circle in img.find_circles(roi = (sx, sy, sw, sh), threshold = CIRCLE_THRESH, x_margin = int(sw/3), y_margin = int(sh/3), r_margin = 100, r_min = circle_min_rad, r_max = min(sw, sh), r_step = 1):
                    ball.circles_detected.append(circle)
            except OSError as e:
                raise OSError(str(e) + f" Used det rad: sx{sx} sy{sy} sw{sw} sh{sh}")
            ball.distance = None  # Bugfix: we want to use the center of a circle for distance, but here we already calculated get_distance(), which is buffered, so it is never recalculated with a circle-center

        # Additional Informations + result for each ball
        for ball in balls:
            v = ball.classification_value
            x, y, w, h = ball.get_screen_rect()

            stdev = ball.histogram.get_statistics().stdev()
            mode = ball.histogram.get_statistics().mode()

            classified_as = ball.classified_as
            histogram_classification = False

            if mode > 100:
                histogram_classification = ball.SILVER
            else:
                histogram_classification = ball.BLACK

            certain = False

            if histogram_classification == classified_as:
                certain = True

            conf = (0.7 * v) + (0.3 * (len(ball.circles_detected)==1)) # (0.2 * certain) +

            ball.confidence = conf
            ball.histogram_classification = histogram_classification

            print(f"Ball: Class:{classified_as} HistoClass:{histogram_classification} x{x} y{y} w{w} h{h} x_off{ball.get_x_offset()} dist{ball.get_distance()} v{v:.3} StDev{stdev} Mode{mode} Confidence{conf}=(0.5 * {v}) + (0.2 * {certain}) + (0.3 * ({len(ball.circles_detected)}==1))")

def rgb_handler():
    global exit_line, img

    if EXIT_LINE_ENABLED:
        exit_line.init(reset=True)
        temp_exit_line_list: list[lib_objects.exit_line] = []

        # Search for green blobs as Exit Lines:
        for b in img.find_blobs([(16, 28, -17, -7, 0, 13)], merge=True, margin=2):
            (x, y, w, h) = b.rect()
            conf = 1.0
            temp_exit_line_list.append( lib_objects.exit_line().init( screen_rect=b.rect(), histogram=img.get_histogram(roi=b.rect()), blob=b, confidence=conf ))
        # Only keep highest confidence line
        if len(temp_exit_line_list)>0:
            exit_line = max(temp_exit_line_list, key=lambda x: x.confidence)
            x, y, w, h = exit_line.get_screen_rect()
            b = exit_line.blob
            print(f"Exit: x{x} y{y} w{w} h{h} x_off{exit_line.get_x_offset()} dist{exit_line.get_distance()} pix{b.pixels()} rot{b.rotation_deg()}° round{b.roundness()} elong{b.elongation()} dens{b.density()} convex{b.convexity()}")

def drawing_handler():
    global balls, corner, exit_line, img

    # Draw Balls
    for ball in balls:
        x, y, w, h = ball.get_screen_rect()
        classified_as = ball.classified_as
        color = 0
        if classified_as == ball.BLACK:
            color = black_ball_id
        else:
            color = silver_ball_id
        img.draw_rectangle(x, y, w, h, colors[color], 1, False)
        img.draw_rectangle(ball.get_screen_det_rad(), colors[color], 1, False)
        for c in ball.circles_detected:
            img.draw_circle(c.x(), c.y(), c.r(), color = colors[color])
        img.draw_cross(ball.get_screen_center_point(), colors[color], 3, 1)
        img.draw_string(x+2, y-9, f"{int(ball.confidence*100)} {int(ball.get_x_offset())}|{int(ball.get_distance())}", color=colors[color], mono_space=False)

    # Draw Corner
    if corner.valid:
        x, y, w, h = corner.get_screen_rect()
        img.draw_rectangle((x, y, w, h), colors[corner_id], 1, False)
        img.draw_cross(corner.get_screen_center_point(), colors[corner_id], 3, 1)
        img.draw_string(x+2, y-9, f"{int(corner.confidence*100)} {int(corner.get_x_offset())}|{int(corner.get_distance())}", color=colors[corner_id], mono_space=False)
    # Draw Exit Line
    if exit_line.valid:
        x, y, w, h = exit_line.get_screen_rect()
        img.draw_rectangle((x, y, w, h), colors[exit_line_id], 1, False)
        img.draw_cross(exit_line.get_screen_center_point(), colors[exit_line_id], 3, 1)
        img.draw_string(x+2, y-9, f"{int(exit_line.confidence*100)} {int(exit_line.get_x_offset())}|{int(exit_line.get_distance())}", color=colors[exit_line_id], mono_space=False)

if __name__ == '__main__':
    clock = time.clock()
    gc.enable()

    #print("Before tof init")
    #init_tof()
    #print("before tof start ranging")
    #start_tof_ranging()
    #print("before init_sensor")
    init_sensor()
    #print("before tf")
    load_tf_models()
    init_colors()
    #print("before omv")
    OMV_DEBUG = usb.isconnected()
    blink_led()

    OMV_DEBUG = DEBUG_IN_IDE and OMV_DEBUG
    #print("before while")
    while(True):
        clock.tick()
        #print("in while before tof")
        #get_tof_results()
        #start_tof_ranging()
        #print("before if")
        if black_white:
            if BALLS_ENABLED or CORNER_ENABLED:
                #print("in balls_or_corner")
                sensor.set_pixformat(sensor.GRAYSCALE)
                img = sensor.snapshot()
                #print("before handler")
                black_white_handler()
                ard_comm.send_gray_data(balls, corner)

                if OMV_DEBUG:
                    omv.disable_fb(True)

            if EXIT_LINE_ENABLED or OMV_DEBUG:
                black_white = False

        else:
            if EXIT_LINE_ENABLED or OMV_DEBUG:
                sensor.set_pixformat(sensor.RGB565)
                img = sensor.snapshot()
                rgb_handler()
                ard_comm.send_rgb_data(exit_line)
                if OMV_DEBUG:
                    drawing_handler()
                    omv.disable_fb(False)

            if BALLS_ENABLED or CORNER_ENABLED:
                black_white = True

        ard_comm.tick()

        print(clock.fps(), "fps", end="\n\n")
