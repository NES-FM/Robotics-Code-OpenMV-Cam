from lib.vl53l5cx import RANGING_MODE_AUTONOMOUS, RANGING_MODE_CONTINUOUS, POWER_MODE_SLEEP, POWER_MODE_WAKEUP
from lib.vl53l5cx import TARGET_ORDER_CLOSEST, TARGET_ORDER_STRONGEST, RESOLUTION_4X4, RESOLUTION_8X8
from lib.vl53l5cx import DATA_AMBIENT_PER_SPAD, DATA_NB_SPADS_ENABLED, DATA_NB_TARGET_DETECTED, DATA_SIGNAL_PER_SPAD, DATA_RANGE_SIGMA_MM, DATA_DISTANCE_MM, DATA_REFLECTANCE, DATA_TARGET_STATUS, DATA_MOTION_INDICATOR
from lib.vl53l5cx import STATUS_VALID
from lib.vl53l5cx import VL53L5CXMP, make_sensor
import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time = 2000)
sensor.set_windowing((240,240))

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

map_index_to_y_pos = {0: 6,
                      1: 7,
                      2: 4,
                      3: 5,
                      4: 2,
                      5: 3,
                      6: 0,
                      7: 1}

def main():
    clock = time.clock()
    tof = make_sensor()
    tof.reset()

    if not tof.is_alive():
        raise ValueError("VL53L5CX not detected")

    tof.init()

    tof.resolution = RESOLUTION_8X8
    tof.ranging_freq = 6
    tof.ranging_mode = RANGING_MODE_AUTONOMOUS
    tof.target_order = TARGET_ORDER_CLOSEST

    grid=7

    tof.start_ranging({DATA_DISTANCE_MM, DATA_TARGET_STATUS})

    while True:
        #print("While")
        if tof.check_data_ready():
            clock.tick()
            snpsht=sensor.snapshot()

            img=image.Image(8, 8, sensor.GRAYSCALE)
            #print("Image")
            results = tof.get_ranging_data()
            distance = results.distance_mm
            status = results.target_status
            #print("tof")

            for i, d in enumerate(distance):
                if status[i] == STATUS_VALID:
                    img.set_pixel(int(i/8), map_index_to_y_pos[i%8], int(distance[i]/10))
                else:
                    img.set_pixel(int(i/8), map_index_to_y_pos[i%8], 255)

            #print("write 1")

            snpsht.draw_image(img, 100, 140, x_size=280, y_size=280, alpha=100, hint=image.CENTER|image.BILINEAR)
            #print("write 2")
            print(clock.fps())
            #print(" ")
        time.sleep_ms(100)

main()
