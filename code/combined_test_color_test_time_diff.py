import sensor, time, tf, math, gc, pyb, omv
import uos # type: ignore
from image import Image
from lib import lib_ard

### CONFIG
OMV_DEBUG = True # Whether to show framebuffer in OpenMV IDE or not
min_confidence = 0.4 # Min Config for TensorFlow Detection
circle_thresh = 1800 # Detection Threshold for circle detection
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
net = None
labels = None

balls: dict
corner: dict
exit_line: dict
img: Image
### ENDGLOBAL

def init_sensor():
    omv.disable_fb(True)
    
    sensor.reset()                         # Reset and initialize the sensor.
    sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
    sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
    sensor.set_windowing((240, 240))        # Set 240x240 window.
    sensor.skip_frames(time=500)          # Let the camera adjust.

def load_tf_models():
    global net, labels, background_id, exit_line_id, silver_ball_id, black_ball_id, corner_id
    try:
        # load the model, alloc the model file on the heap if we have at least 64K free after loading
        net = tf.load("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))  # type: ignore
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

def black_white_handler():
    global balls, corner, img
    balls.clear()
    corner.clear()

    # Tensorflow detection
    for i, detection_list in enumerate(net.detect(img, thresholds=[(math.ceil(min_confidence * 255), 255)])):
        if (i == 0): continue # background class
        if (len(detection_list) == 0): continue # no detections for this class?

        for d in detection_list:
            if i == black_ball_id:  # black ball
                balls[d.rect()] = {"classified_as": "black", "value": d.output(), "circles": [], "histogram": img.get_histogram(roi=d.rect()), "conf": -1, "histo_class": "unknown"}
            elif i == corner_id:  # corner
                corner[d.rect()] = {"classified_as": "corner", "value": d.output(), "circles": [], "histogram": img.get_histogram(roi=d.rect()), "blob": None}
            elif i == silver_ball_id:  # silver_ball
                balls[d.rect()] = {"classified_as": "silver", "value": d.output(), "circles": [], "histogram": img.get_histogram(roi=d.rect()), "conf": -1, "histo_class": "unknown"}
                
    # For every ball found, search for circles within the area
    for (x, y, w, h), data in balls.copy().items():
        sx, sy, sw, sh = x-16, y-16, w+32, h+32
        for c in img.find_circles(roi = (sx, sy, sw, sh), threshold = circle_thresh, x_margin = int(sw/3), y_margin = int(sh/3), r_margin = 100, r_min = 5, r_max = min(sw, sh), r_step = 1):
            balls[(x, y, w, h)]["circles"].append(c)
            
    # Search for black blobs as corners:
    for b in img.find_blobs([(0, 17)], merge=True, margin=5):
        (x, y, w, h) = b.rect()
        if b.pixels() > 2000: # and x > 15 and (x+w) < (240-15) and y > 15 and (y+h) < (240-15):
            conf = ((1-b.roundness()) * 0.5) + (b.elongation() * 0.5)
            if conf > 0.8:
                corner[b.rect()] = {"classified_as": "corner", "value": 1, "circles": [], "histogram": img.get_histogram(roi=b.rect()), "blob": b, "conf": conf}
                print(f"Corner:Blob x{x} y{y} w{w} h{h} conf{conf} pix{b.pixels()} rot{b.rotation_deg()}° round{b.roundness()} elong{b.elongation()} dens{b.density()} convex{b.convexity()}")
    # Only keep highest confidence corner
    for key, _ in sorted(corner.items(), key=lambda x:x[1]["conf"])[:-1]:
        corner.pop(key)
    """In Honor of ChatGPT for coming up with a more efficient, but more unreadable solution:
    # Find the key with the maximum "conf" value in the dictionary
    max_key = max(corner, key=lambda x: corner[x]["conf"])

    # Use the key to find the corresponding key-value pair in the dictionary
    max_pair = corner[max_key]

    # Remove all other key-value pairs from the dictionary
    corner.clear()
    corner[max_key] = max_pair
    """
                
    # Additional Informations + result for each ball
    for rec, data in balls.copy().items():
        v = data["value"]
        x, y, w, h = rec

        stdev = data["histogram"].get_statistics().stdev()
        #mean = data["histogram"].get_statistics().mean()
        #median = data["histogram"].get_statistics().median()
        mode = mean = data["histogram"].get_statistics().mode()

        classified_as = data["classified_as"]
        histogram_classification = ""
        if mode > 100:
            histogram_classification = "silver"
        else:
            histogram_classification = "black"
        certain = False
        if histogram_classification == classified_as:
            certain = True
        conf = (0.5 * v) + (0.2 * certain) + (0.3 * (len(data["circles"])==0))# + min((stdev / 50)*0.25, 0.25)

        balls[rec]["conf"] = conf
        balls[rec]["histo_class"] = histogram_classification

        print(f"Ball: Class:{classified_as} HistoClass:{histogram_classification} x{x} y{y} w{w} h{h} v{v:.3} StDev{stdev} Mode{mode} Confidence{conf}=(0.5 * {v}) + (0.2 * {certain}) + (0.3 * ({len(data['circles'])}>0))")

def rgb_handler():
    global exit_line, img
    exit_line.clear()

    # Search for green blobs as Exit Lines:
    for b in img.find_blobs([(16, 28, -17, -7, 0, 13)], merge=True, margin=2):
        (x, y, w, h) = b.rect()
        exit_line[b.rect()] = {"classified_as": "exit", "value": 1, "circles": [], "histogram": img.get_histogram(roi=b.rect()), "blob": b, "conf": 1}
        print(f"Exit: x{x} y{y} w{w} h{h} pix{b.pixels()} rot{b.rotation_deg()}° round{b.roundness()} elong{b.elongation()} dens{b.density()} convex{b.convexity()}")
    # Only keep highest confidence line
    for key, _ in sorted(exit_line.items(), key=lambda x:x[1]["conf"])[:-1]:
        exit_line.pop(key)

def drawing_handler():
    global balls, corner, exit_line, img

    # Draw Balls
    for (x, y, w, h), data in balls.items():
        classified_as = data["classified_as"]
        color = 0
        if classified_as == "black":
            color = black_ball_id
        else:
            color = silver_ball_id
        img.draw_rectangle(x, y, w, h, colors[color], 1, False)
        for c in data["circles"]:
            img.draw_circle(c.x(), c.y(), c.r(), color = colors[color])
    # Draw Corner
    for (x, y, w, h), data in corner.items():
        img.draw_rectangle(x, y, w, h, colors[corner_id], 1, False)
    # Draw Exit Line
    for (x, y, w, h), data in exit_line.items():
        img.draw_rectangle(x, y, w, h, colors[exit_line_id], 1, False)

if __name__ == '__main__':
    clock = time.clock()  # type: ignore
    gc.enable()

    init_sensor()
    
    load_tf_models()
    init_colors()
    
    while(True):
        clock.tick()

        if black_white:
            sensor.set_pixformat(sensor.GRAYSCALE)
            img = sensor.snapshot()
            black_white_handler()
            if OMV_DEBUG:
                omv.disable_fb(True)
        else:
            sensor.set_pixformat(sensor.RGB565)
            img = sensor.snapshot()
            rgb_handler()
            if OMV_DEBUG:
                drawing_handler()
                omv.disable_fb(False)
        black_white = not black_white

        print(clock.fps(), "fps", end="\n\n")
