from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
import time

leftT = TouchSensor(INPUT_4)
rightT = TouchSensor(INPUT_1)

bttn = Button()
snd = Sound()

while not bttn.backspace:
    leftVal = leftT.is_pressed
    rightVal = rightT.is_pressed
    print(leftVal, rightVal)
    if leftVal == 1 and rightVal == 1:
        snd.tone([(440, 100, 0.0), (880, 100, 0.0)])
    elif leftVal == 1:
        snd.play_tone(440, 0.1, 0.0)
    elif rightVal == 1:
        snd.play_tone(880, 0.1, 0.0)
    time.sleep(0.1)
