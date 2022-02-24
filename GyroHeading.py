from ev3dev2.motor import LargeMotor, MoveTank
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button

tank = MoveTank(OUTPUT_C, OUTPUT_B)
gs = GyroSensor(INPUT_1)
bttn = Button()

turn_power = 10
tol = 2

def enter_pressed():
    while True:
        if bttn.backspace:
            return False
        if bttn.enter:
            return True

def is_within(actual, desired, tolerance):
    return (desired - tolerance) < actual < (desired + tolerance)


def do_the_thing(heading):
    tank.on(10, -10)
    curr_heading = gs.angle
    while not is_within(curr_heading % 360, heading, tol):
        curr_heading = gs.angle
        print(curr_heading % 360)
        if bttn.backspace:
            break
    tank.off()


print("first heading:", gs.angle)
do_the_thing(0)
enter_pressed() # waits until enter is pressed
do_the_thing(65)