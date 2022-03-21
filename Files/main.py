from time import sleep
import keyboard
from string import * # модуль для упрошённой работы  разными символами
from pyautogui import screenshot
from random import *
syms = list(ascii_letters) # буквы
nums = list(str(digits)) # цифры
sleep(5)
while True:
    shuffle(nums)
    shuffle(syms)
    code = nums + syms
    shuffle(code)
    code = "".join(code)
    keyboard.press('t')
    keyboard.release('t')
    sleep(0.1)
    keyboard.write(f'/warp {code}')
    keyboard.send('enter')
    sleep(3)
    keyboard.press('t')
    keyboard.release('t')
    sleep(0.1)
    keyboard.write('/tp @s 0 80 0')
    keyboard.send('enter')
    sleep(3)
    screenshot(f'screnshots\{code}.png')