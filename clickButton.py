import pyautogui
import time

def click_flow():
    pyautogui.click(760, 392)
    time.sleep(0.5)
    pyautogui.click(677, 299)
    time.sleep(1)

for i in range(2):
    click_flow()