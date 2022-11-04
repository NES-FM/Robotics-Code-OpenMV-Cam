# Record Dataset - By: flori - Fr Nov 4 2022

import sensor, image, time, pyb, uos

sensor.reset()
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_windowing((240, 240))
sensor.skip_frames(time = 2000)

dir_name = "images/"

try:
    uos.mkdir(dir_name)
except OSError:
    print("Folder already exists")

i = 0  # Start value

try:
    with open("last_img.txt", "r") as f:
        i = int(f.readlines()[0])+1
except OSError:
    print("Using default of i = 0")

while(True):
    pyb.LED(1).off()
    time.sleep_ms(10)

    img = sensor.snapshot().bilateral(2, color_sigma=0.1, space_sigma=1)
    img.save(f"{dir_name}/img_{i:0>3}.bmp")
    with open("last_img.txt", "w") as f:
        f.write(str(i))

    time.sleep_ms(10)
    pyb.LED(1).on()
    time.sleep_ms(400)

    i += 1
