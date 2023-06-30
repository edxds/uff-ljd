from vendor.pplay.window import Window


def GameOver(window: Window):
    _duration = 0

    while True:
        _duration += window.delta_time()

        if _duration > 3:
            return

        window.set_background_color([0, 0, 0])
        window.draw_text("Game over", window.width / 2 - 60, window.height / 2 - 32, 32, [255, 255, 255])
        window.update()
