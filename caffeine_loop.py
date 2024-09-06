from pyautogui import moveRel
from time import sleep

while True:
    moveRel(10, 10, duration=0.25)
    # sleep(10)
    moveRel(-10, -10, duration=0.25)
    sleep(10)