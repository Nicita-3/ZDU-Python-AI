import pyautogui
import random
import time
import keyboard

screen_width, screen_height = pyautogui.size()

def smooth_move(x1, y1, x2, y2, steps=400):
    for i in range(steps + 1):
        if keyboard.is_pressed("q"):
            return False

        t = i / steps
        offset_x = random.uniform(-5, 5)
        offset_y = random.uniform(-5, 5)
        x = int(x1 + (x2 - x1) * t + offset_x)
        y = int(y1 + (y2 - y1) * t + offset_y)
        pyautogui.moveTo(x, y)
        time.sleep(0.01)

    return True

while True:
    if keyboard.is_pressed("q"):
        break

    start_x, start_y = pyautogui.position()

    target_x = random.randint(0, screen_width - 1)
    target_y = random.randint(0, screen_height - 1)

    if not smooth_move(start_x, start_y, target_x, target_y, steps=random.randint(300, 500)):
        break