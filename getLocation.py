import pyautogui
import keyboard
import time

print("Move mouse and press 'p' to print position, ESC to exit")

while True:
    if keyboard.is_pressed('p'):
        print(pyautogui.position())
        time.sleep(0.3)

    if keyboard.is_pressed('esc'):
        break