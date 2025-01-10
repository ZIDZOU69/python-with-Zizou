import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="t")

clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.12)
def toggle_event(Key):
    if Key == TOGGLE_KEY:
        global clicking
        clicking = not clicking




click_thrad = threading.Thread(target=clicker)
click_thrad.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()