import pyautogui
from pyautogui import locateOnScreen as LoS
from time import sleep

while True:
    TOTAL = LoS('total.png', confidence =0.8)
    if TOTAL:
        sleep(2)
        x, y = pyautogui.locateCenterOnScreen('text.png', confidence =0.8)
        pyautogui.click(x, y)
        pyautogui.write('cupomvalido20')
        sleep(1)
        z, t = pyautogui.locateCenterOnScreen('utilizar.png', confidence =0.8)
        pyautogui.click(z, t)
    else:
        break
       