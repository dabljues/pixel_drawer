import numpy as np
import pynput.keyboard
import pynput.mouse
from pynput.keyboard import Key, Listener
from pynput.mouse import Button
from time import sleep

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()


def on_press(key):
    if key == Key.f9 or key == Key.f10:
        return False


def draw(image_array: np.array) -> None:
    print(image_array)
    with Listener(on_press=on_press) as listener:
        listener.join()
    x, y = mouse.position
    for r, row in enumerate(image_array):
        for c, col in enumerate(row):
            if col:
                mouse.position = (x + c, y + r)
                mouse.click(Button.left, 1)
                sleep(0.0001)
