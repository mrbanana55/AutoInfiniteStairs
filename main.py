import pyautogui
import time
import keyboard

#left stair position x: 864 y: 715
#right stair position x: 1004 y: 715
#color RGB (102, 85, 85)


while keyboard.is_pressed('q') == False:

    time.sleep(10)
    
    #press z to make the first step
    pyautogui.press('z')

    #checks if there is a stair to the left
    if pyautogui.pixel(864, 715)[0] == 102 and pyautogui.pixel(864, 715)[1] == 85 and pyautogui.pixel(864, 715)[2] == 85:
        pyautogui.press('z')
        time.sleep(0.5)
    else: 
        pyautogui.press('x')
        time.sleep(0.5)

    #checks if there is a stair to the right
    if pyautogui.pixel(1004, 715)[0] == 102 and pyautogui.pixel(864, 715)[1] == 85 and pyautogui.pixel(864, 715)[2] == 85:
        pyautogui.press('z')
        time.sleep(0.5)
    else:
        pyautogui.press('x')
        time.sleep(0.5)