#como simular rolagem 
import pyautogui
from time import sleep

pyautogui.moveTo(1470,571,duration=2)
pyautogui.scroll(-1500)
for i in range(500):
    pyautogui.scroll(-1500)
    sleep(2)
