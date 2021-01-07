from pyautogui import *
import pyautogui 
import time
import keyboard
import random
import win32api, win32con

## This will place blocks like so: https://www.youtube.com/watch?v=LLBX3V1WrR8

##Top: Y = 80
## Bottom = 1002q

x= 960
TopY= 80
BotY = 1000
Delay = 0.01

def PlaceBlock():
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.001)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def Look(dir):
    for i in range(3):
        win32api.SetCursorPos((x,dir))
        time.sleep(0.001)

try:
    while keyboard.is_pressed('q') == False:
        while keyboard.is_pressed('v') == True:
            PlaceBlock()
            time.sleep(Delay)
            Look(TopY)
            time.sleep(Delay)
            PlaceBlock()
            time.sleep(Delay)
            Look(BotY)
            time.sleep(Delay)
            keyboard.press('d')
            
          
except :
    pass  