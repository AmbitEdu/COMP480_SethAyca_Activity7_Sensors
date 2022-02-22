from ev3dev2.motor import LargeMotor, MoveTank, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound

tank = MoveTank(OUTPUT_C, OUTPUT_B)
bttn = Button()
cs = ColorSensor(INPUT_2)
snd = Sound()

drive_power = 10
end_color = cs.COLOR_BLUE

colors_seen = []

tank.on(drive_power, drive_power)
while not bttn.backspace:
    curr_color_code = cs.color
    curr_color = cs.color_name
    print(curr_color_code, curr_color)
    if not curr_color in colors_seen:
        colors_seen.append(curr_color)
        snd.speak(curr_color, play_type=0)
    if curr_color_code == end_color:
        break
tank.off()