from ev3dev2.motor import LargeMotor, MoveTank, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button

tank = MoveTank(OUTPUT_C, OUTPUT_B)
bttn = Button()
cs = ColorSensor(INPUT_2)

turn_power = 10

tank.on(turn_power, -turn_power)
while not bttn.backspace:
    intensity = cs.reflected_light_intensity
    print(intensity)
    if intensity < 10:
        break

tank.off()