import sensor, image, time, os, tf, math, uos, gc, pyb

#pyb.LED(4).on()

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
#sensor.skip_frames(time=2000)          # Let the camera adjust.

net = None
labels = None
min_confidence = 0.3

try:
    # load the model, alloc the model file on the heap if we have at least 64K free after loading
    net = tf.load("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))
except Exception as e:
    raise Exception('Failed to load "trained.tflite", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

try:
    labels = [line.rstrip('\n') for line in open("labels.txt")]
except Exception as e:
    raise Exception('Failed to load "labels.txt", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

colors = [ # Add more colors if you are detecting more than 7 types of classes at once.
    (255,   0,   0),
    (  0, 255,   0),
    (255, 255,   0),
    (  0,   0, 255),
    (255,   0, 255),
    (  0, 255, 255),
    (255, 255, 255),
]

#colors = [
    #235,
    #128,
    #64,
    #200,
    #0
#]

circle_thresh = 1800

grayscale_thres = (0, 136)

w = sensor.width()
h = sensor.height()

TARGET_POINTS = [(0,   0),   # (x, y) CHANGE ME!
                 (w-1, 0),   # (x, y) CHANGE ME!
                 (w+47, h-1), # (x, y) CHANGE ME!
                 (0-48,   h-1)] # (x, y) CHANGE ME!


clock = time.clock()
while(True):
    clock.tick()

    #img = sensor.snapshot().lens_corr(1.5)#.gamma_corr()

    # Lens Corr: MT+2.1=1.5 OV+2.1=2.2
    #img = sensor.snapshot().lens_corr(2.2).rotation_corr(corners = TARGET_POINTS).crop(roi=(40, 0, 240, 240)).gaussian(2).histeq(False)
    #img = sensor.snapshot().rotation_corr(corners = TARGET_POINTS).crop(roi=(40, 0, 240, 240)).gaussian(2)#.histeq(False)
    img = sensor.snapshot()#.histeq(False)

    #second = img.binary([grayscale_thres], copy=True)
    #for i in range(4):
        #second.dilate(2)
    #for i in range(2):
        #second.erode(2)

    #second.invert()
    #img.replace(int(0.75*255), mask=second)


    balls = {}
    corner = {}

    # Tensorflow detection
    for i, detection_list in enumerate(net.detect(img, thresholds=[(math.ceil(min_confidence * 255), 255)])):
        if (i == 0): continue # background class
        if (len(detection_list) == 0): continue # no detections for this class?

        for d in detection_list:
            if i == 1:  # black ball
                balls[d.rect()] = {"classified_as": "black", "value": d.output(), "circles": [], "histogram": img.get_histogram(roi=d.rect())}
            elif i == 2:  # corner
                corner[d.rect()] = {"classified_as": "corner", "value": d.output(), "circles": [], "histogram": img.get_histogram(roi=d.rect()), "blob": None}
            elif i == 3:  # silver_ball
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

        color = 2
        certain = False
        if histogram_classification == classified_as:
            certain = True
            color = 0 if classified_as == "black" else 1

        conf = (0.5 * v) + (0.2 * certain) + (0.3 * (len(data["circles"])>0))# + min((stdev / 50)*0.25, 0.25)

        print(f"Ball: Class:{classified_as} HistoClass:{histogram_classification} x{x} y{y} w{w} h{h} v{v:.3} StDev{stdev} Mode{mode} Confidence{conf}=(0.5 * {v}) + (0.2 * {certain}) + (0.3 * ({len(data['circles'])}>0))")

        img.draw_rectangle(x, y, w, h, colors[color], 1, False)
        for c in data["circles"]:
            img.draw_circle(c.x(), c.y(), c.r(), color = colors[color])

    for (x, y, w, h), data in corner.items():
        v = data["value"]
        if isinstance(data["blob"], type(None)):
            print(f"Corner:TF x{x} y{y} w{w} h{h} v{v}")
        else:
            b = data["blob"]
            print(f"Corner:Blob x{x} y{y} w{w} h{h} pix{b.pixels()} rot{b.rotation_deg()}° round{b.roundness()} elong{b.elongation()} dens{b.density()} convex{b.convexity()}")
        img.draw_rectangle(x, y, w, h, colors[3], 1, False)


    #img.draw_string(2, 220, "BB", colors[0], 2, mono_space = False)
    #img.draw_string(30, 220, "SB", colors[1], 2, mono_space = False)
    #img.draw_string(60, 220, "CO", colors[2], 2, mono_space = False)

    print(clock.fps(), "fps", end="\n\n")
