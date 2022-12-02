# Erode and Dilate Example
#
# This example shows off the erode and dilate functions which you can run on
# a binary image to remove noise. This example was originally a test but its
# useful for showing off how these functions work.

import pyb, sensor, image, time

#pyb.LED(4).on()

sensor.reset()
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_windowing((240, 240))
#sensor.set_auto_whitebal(False)
#sensor.set_auto_exposure(False, 25000)
sensor.skip_frames(time = 2000) # Let new settings take affect.

grayscale_thres = (0, 103)

w = sensor.width()
h = sensor.height()

clock = time.clock() # Tracks FPS.

TARGET_POINTS = [(0,   0),   # (x, y) CHANGE ME!
                 (w-1, 0),   # (x, y) CHANGE ME!
                 (w+47, h-1), # (x, y) CHANGE ME!
                 (0-48,   h-1)] # (x, y) CHANGE ME!

while(True):
    clock.tick()

    #img = sensor.snapshot().rotation_corr(corners = TARGET_POINTS).crop(roi=(40, 0, 240, 240)).bilateral(2, color_sigma=0.1, space_sigma=1)#.gaussian(2)#.histeq(False)
    img = sensor.snapshot().bilateral(2, color_sigma=0.1, space_sigma=1)

    #second = img.binary([grayscale_thres], copy=True)
    #for i in range(4):
        #second.dilate(2)
    #for i in range(2):
        #second.erode(2)

    #second.invert()
    #img.replace(int(0.75*255), mask=second)

    #for c in img.find_circles(threshold = 2000, x_margin = 10, y_margin = 10, r_margin = 30,
            #r_min = 2, r_max = 100, r_step = 2):
        #img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))
        #print(c)

    print(clock.fps())
