import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

w = sensor.width()
h = sensor.height()

TARGET_POINTS = [(0,   0),   # (x, y) CHANGE ME!
                 (w-1, 0),   # (x, y) CHANGE ME!
                 (w+47, h-1), # (x, y) CHANGE ME!
                 (0-48,   h-1)] # (x, y) CHANGE ME!

while(True):
    clock.tick()

    img = sensor.snapshot().lens_corr(1.5).rotation_corr(corners = TARGET_POINTS).crop(roi=(40, 0, 240, 240)).gaussian(2).histeq(False)

    #for c in img.find_circles(threshold = 2000, x_margin = 10, y_margin = 10, r_margin = 10,
            #r_min = 2, r_max = 100, r_step = 2):
        #img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))
        #print(c)

    print(clock.fps())
