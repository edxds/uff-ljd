from vendor.pplay.window import Window


def Game(window: Window):
    keyboard = window.get_keyboard()

    while True:
        window.set_background_color([0, 0, 0])

        if keyboard.key_pressed("ESC"):
            return

        window.update()
