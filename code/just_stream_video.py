# Untitled - By: flori - Mi Dez 21 2022

import sensor, image, time

X_OFFSET_WINDOWING = 70  # Range: 0-80

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.set_windowing((X_OFFSET_WINDOWING, 0, 240, 240))        # Set 240x240 window.
sensor.skip_frames(time=500)          # Let the camera adjust.

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
