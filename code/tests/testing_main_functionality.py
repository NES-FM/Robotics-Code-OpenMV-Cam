# Untitled - By: flori - Di Dez 27 2022

import sensor, image, time, pyb

red_led = pyb.LED(1)
blue_led = pyb.LED(3)

usb = pyb.USB_VCP()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    if usb.isconnected():
        red_led.on()
        blue_led.off()
    else:
        red_led.off()
        blue_led.on()
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
