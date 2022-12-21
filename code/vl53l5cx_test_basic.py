from lib.vl53l5cx import DATA_TARGET_STATUS, DATA_DISTANCE_MM
from lib.vl53l5cx import STATUS_VALID, RESOLUTION_4X4, RESOLUTION_8X8
from lib.vl53l5cx import VL53L5CXMP, make_sensor
from machine import I2C, Pin

def main():
    tof = make_sensor()
    tof.reset()

    if not tof.is_alive():
        raise ValueError("VL53L5CX not detected")

    tof.init()

    tof.resolution = RESOLUTION_8X8
    grid = 7

    tof.ranging_freq = 2

    tof.start_ranging({DATA_DISTANCE_MM, DATA_TARGET_STATUS})

    while True:
        if tof.check_data_ready():
            results = tof.get_ranging_data()
            distance = results.distance_mm
            status = results.target_status

            for i, d in enumerate(distance):
                if status[i] == STATUS_VALID:
                    print("{:4}".format(d), end=" ")
                else:
                    print("0000", end=" ")

                if (i & grid) == grid:
                    print("")

            print("----")


main()
