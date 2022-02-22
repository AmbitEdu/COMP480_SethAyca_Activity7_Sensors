from ev3dev2.motor import LargeMotor, MoveTank, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.button import Button

bttn = Button()
tank = MoveTank(OUTPUT_C, OUTPUT_B)
us = UltrasonicSensor(INPUT_3)

drive_power = 10

def enter_pressed():
    while True:
        if bttn.backspace:
            return False
        if bttn.enter:
            return True

def move_towards_wall(distance):
    tank.on(drive_power, drive_power)
    while not bttn.backspace:
        if us.distance_centimeters < distance:
            break
    tank.off()

move_towards_wall(15)
if enter_pressed():
    move_towards_wall(10)
if enter_pressed():
    move_towards_wall(5)
# if enter_pressed():
#     move_towards_wall(3)
# 3 centimeters was a bit too close. The sensor appeared to be only 1 to 1.5 cm away from the wall, but pressed on
# anyway. Once stuck up against the wall, it just mindlessly spun on until we interrupted the program with the backspace
# button. We didn't notice a difference in behavior between the wall and the tub, though it's not difficult to imagine
# that the performance of the ultrasonic sensor is probably influenced by the sonic reflectivity of the material.
