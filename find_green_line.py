# Untitled - By: flori - So Nov 13 2022

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((240, 240))       # Set 240x240 window.


clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot().bilateral(2, color_sigma=0.1, space_sigma=1)

    for b in img.find_blobs([(0, 43, -128, -11, -128, 127)], merge=True, margin=10):
        (x, y, w, h) = b.rect()
        img.draw_rectangle(x, y, w, h, color=(255, 0, 0))
    print(clock.fps())
