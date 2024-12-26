#como preencher um campo automaticamente com digitação 
import pyautogui
from time import sleep
# from mouseinfo import mouseInfo
# mouseInfo()

pyautogui.moveTo(121,43, duration=1)
pyautogui.doubleClick()
sleep(1)
pyautogui.press('tab')
pyautogui.typewrite('a123456')