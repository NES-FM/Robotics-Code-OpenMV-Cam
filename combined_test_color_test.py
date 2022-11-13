import sensor, image, time, os, tf, math, uos, gc, pyb, omv

OMV_DEBUG = True

#omv.disable_fb(True)

#pyb.LED(4).on()

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))        # Set 240x240 window.
#sensor.skip_frames(time=2000)          # Let the camera adjust.

net = None
labels = None
min_confidence = 0.2

background_id = 0
exit_line_id = 10
silver_ball_id = 11
black_ball_id = 12
corner_id = 13

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

colors = [(0, 0, 0)] * 15
colors[black_ball_id]  = (255, 0,   0  )
colors[exit_line_id]   = (0,   255, 0  )
colors[silver_ball_id] = (0,   0,   255)
colors[corner_id]      = (255, 255, 0  )

circle_thresh = 1800

grayscale_thres = (0, 136)

w = sensor.width()
h = sensor.height()

TARGET_POINTS = [(0,   0),   # (x, y) CHANGE ME!
                 (w-1, 0),   # (x, y) CHANGE ME!
                 (w+47, h-1), # (x, y) CHANGE ME!
                 (0-48,   h-1)] # (x, y) CHANGE ME!

clock = time.clock()

def get_images_using_copy():
    omv.disable_fb(False)
    img_rgb = sensor.snapshot()#.bilateral(2, color_sigma=0.1, space_sigma=1)
    img = img_rgb.to_grayscale(copy=True)
    return (img_rgb, img)

def get_images_individual():
    omv.disable_fb(False)
    sensor.set_pixformat(sensor.GRAYSCALE)
    img = sensor.snapshot()

    omv.disable_fb(True)
    sensor.set_pixformat(sensor.RGB565)
    img_rgb = sensor.snapshot()#.bilateral(2, color_sigma=0.1, space_sigma=1)

    return (img_rgb, img)

while(True):
    clock.tick()

    img_rgb, img = get_images_using_copy()

    balls = {}
    corner = {}
    exit_line = {}

    # Tensorflow detection
    for i, detection_list in enumerate(net.detect(img, thresholds=[(math.ceil(min_confidence * 255), 255)])):
        if (i == 0): continue # background class
        if (len(detection_list) == 0): continue # no detections for this class?

        for d in detection_list:
            if i == black_ball_id:  # black ball
                balls[d.rect()] = {"classified_as": "black", "value": d.output(), "circles": [], "histogram": img.get_histogram(roi=d.rect())}
            elif i == corner_id:  # corner
                corner[d.rect()] = {"classified_as": "corner", "value": d.output(), "circles": [], "histogram": img.get_histogram(roi=d.rect()), "blob": None}
            elif i == silver_ball_id:  # silver_ball
                balls[d.rect()] = {"classified_as": "silver", "value": d.output(), "circles": [], "histogram": img.get_histogram(roi=d.rect())}


    # For every ball found, search for circles within the area
    for (x, y, w, h), data in balls.copy().items():
        sx, sy, sw, sh = x-16, y-16, w+32, h+32
        for c in img.find_circles(roi = (sx, sy, sw, sh), threshold = circle_thresh, x_margin = int(sw/3), y_margin = int(sh/3), r_margin = 100, r_min = 5, r_max = min(sw, sh), r_step = 1):
            balls[(x, y, w, h)]["circles"].append(c)

    # Search for black blobs as corners:
    for b in img.find_blobs([(0, 17)], merge=True, margin=3):
        (x, y, w, h) = b.rect()
        if x > 15 and (x+w) < (240-15) and y > 15 and (y+h) < (240-15) and b.pixels() > 500:
            corner[b.rect()] = {"classified_as": "corner", "value": 1, "circles": [], "histogram": img.get_histogram(roi=b.rect()), "blob": b}

    # Search for green blobs as Exit Lines:
    for b in img_rgb.find_blobs([(16, 28, -17, -7, 0, 13)], merge=True, margin=2):
        (x, y, w, h) = b.rect()
        exit_line[b.rect()] = {"classified_as": "corner", "value": 1, "circles": [], "histogram": img.get_histogram(roi=b.rect()), "blob": b}

    omv.disable_fb(True)
    img_rgb = sensor.snapshot()

    ## Drawing
    for (x, y, w, h), data in balls.items():
        v = data["value"]
        stdev = data["histogram"].get_statistics().stdev()
        mean = data["histogram"].get_statistics().mean()
        median = data["histogram"].get_statistics().median()
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

        color = 0
        if classified_as == "black":
            color = black_ball_id
        else:
            color = silver_ball_id

        conf = (0.5 * v) + (0.2 * certain) + (0.3 * (len(data["circles"])>0))# + min((stdev / 50)*0.25, 0.25)

        print(f"Ball: Class:{classified_as} HistoClass:{histogram_classification} x{x} y{y} w{w} h{h} v{v:.3} StDev{stdev} Mode{mode} Confidence{conf}=(0.5 * {v}) + (0.2 * {certain}) + (0.3 * ({len(data['circles'])}>0))")

        img_rgb.draw_rectangle(x, y, w, h, colors[color], 1, False)
        for c in data["circles"]:
            img_rgb.draw_circle(c.x(), c.y(), c.r(), color = colors[color])

    for (x, y, w, h), data in corner.items():
        v = data["value"]
        if isinstance(data["blob"], type(None)):
            print(f"Corner:TF x{x} y{y} w{w} h{h} v{v}")
        else:
            b = data["blob"]
            print(f"Corner:Blob x{x} y{y} w{w} h{h} pix{b.pixels()} rot{b.rotation_deg()}° round{b.roundness()} elong{b.elongation()} dens{b.density()} convex{b.convexity()}")
        img_rgb.draw_rectangle(x, y, w, h, colors[corner_id], 1, False)

    for (x, y, w, h), data in exit_line.items():
        v = data["value"]
        b = data["blob"]
        print(f"Exit: x{x} y{y} w{w} h{h} pix{b.pixels()} rot{b.rotation_deg()}° round{b.roundness()} elong{b.elongation()} dens{b.density()} convex{b.convexity()}")
        img_rgb.draw_rectangle(x, y, w, h, colors[exit_line_id], 1, False)

    print(clock.fps(), "fps", end="\n\n")
