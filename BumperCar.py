from ev3dev2.motor import LargeMotor, MoveTank, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.button import Button
import time

leftT = TouchSensor(INPUT_4)
rightT = TouchSensor(INPUT_1)
tank = MoveTank(OUTPUT_C, OUTPUT_B)
bttn = Button()

forward_power = 20
turn_power = 20
turn_time = 0.85

def go_forward():
    tank.on(forward_power, forward_power)

def move_back(time):
    tank.on_for_seconds(-turn_power, -turn_power, time)

def turn_180():
    tank.on_for_seconds(turn_power, -turn_power, 3)

def turn_right():
    tank.on_for_seconds(turn_power, -turn_power, turn_time)

def turn_left():
    tank.on_for_seconds(-turn_power, turn_power, turn_time)

go_forward()
while not bttn.backspace:
    leftVal = leftT.is_pressed
    rightVal = rightT.is_pressed
    if leftVal == 1 and rightVal == 1:
        move_back(3)
        turn_180()
    elif leftVal == 1:
        move_back(1.5)
        turn_right()
    elif rightVal == 1:
        move_back(1.5)
        turn_left()
    go_forward()

tank.off()
