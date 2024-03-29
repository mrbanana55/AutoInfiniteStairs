#meant to be used with https://infinitestairs.io/
import pyautogui
import time
import keyboard

#right stair position x: 1004 y: 744
#color RGB (255, 85, 85)


#checks wether the first step is to the right or to the left
def checkInitialDirection():
    if pyautogui.pixel(864, 744)[0] == 255 and pyautogui.pixel(864, 744)[1] == 255 and pyautogui.pixel(864, 744)[2] == 221:
        direction = "left"
    elif pyautogui.pixel(1004, 744)[0] == 255 and pyautogui.pixel(1004, 744)[1] == 255 and pyautogui.pixel(1004, 744)[2] == 221:
        direction = "right"

    return direction

def changeDirection(direction):
    if direction == "left":
        direction = "right"
    else:
        direction = "left"
    return direction

def goAhead(direction): #press z to make one step in case it sees one stair ahead. If it doesn't then it changes the direction
    if direction == "left":
        if pyautogui.pixel(864, 744)[0] == 255 and pyautogui.pixel(864, 744)[1] == 255 and pyautogui.pixel(864, 744)[2] == 221:
            pyautogui.press('z')
            direction = "left"

        else:
            pyautogui.press('x')
            changeDirection(direction)
            direction = "right"

    elif direction == "right":
        if pyautogui.pixel(1004, 744)[0] == 255 and pyautogui.pixel(1004, 744)[1] == 255 and pyautogui.pixel(1004, 744)[2] == 221:
            pyautogui.press('z')
            direction = "right"

        else:
            pyautogui.press('x')
            changeDirection(direction)
            direction = "left"
    return direction
#if true, keep the same direction. If false, change direction

#main code
time.sleep(3) #waits 3 seconds before it starts working
initial_direction = checkInitialDirection()
#press z to make the first step
pyautogui.press('z')
time.sleep(0.44)
go_ahead = goAhead(initial_direction)
time.sleep(0.44)
while keyboard.is_pressed('q') == False:
    go_ahead = goAhead(go_ahead)
    time.sleep(0.44)

