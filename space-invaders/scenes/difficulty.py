from vendor.pplay.sprite import Sprite
from vendor.pplay.window import Window

from layout import center_in_window, center_x_in_window


def Difficulty(window: Window):
    keyboard = window.get_keyboard()

    easy = Sprite("assets/difficulty/easy.png")
    normal = Sprite("assets/difficulty/normal.png")
    hard = Sprite("assets/difficulty/hard.png")

    center_in_window(normal, window)
    center_x_in_window(easy, window)
    center_x_in_window(hard, window)

    easy.y = normal.y - easy.height - 24
    hard.y = normal.y + hard.height + 24

    while True:
        window.set_background_color([0, 0, 0])
        
        if keyboard.key_pressed("ESC"):
            return

        for btn in [easy, normal, hard]:
            btn.draw()

        window.update()
