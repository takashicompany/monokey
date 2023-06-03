print("Monokey Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.handlers.sequences import send_string

_KEY_CFG = [
    board.A1
]

# Keyboard implementation class
class Monokey(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=_KEY_CFG,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.02,  # Debounce time in floating point seconds
            max_events=64
        )

keyboard = Monokey()

MyKey = send_string("This is Monokey.")

keyboard.keymap = [
    [MyKey]
]

if __name__ == '__main__':
    keyboard.go()