from vendor.pplay.sprite import Sprite
from vendor.pplay.window import Window

from scenes.difficulty import Difficulty
from scenes.game import Game

from layout import center_x_in_window


def main():
    window = Window(1280, 720)

    exit_btn = Sprite("assets/menu/exit.png")
    exit_btn.y = window.height - exit_btn.height - 64
    exit_hover = Sprite("assets/menu/exit-hover.png")

    ranking = Sprite("assets/menu/ranking.png")
    ranking.y = exit_btn.y - ranking.height - 24
    ranking_hover = Sprite("assets/menu/ranking-hover.png")

    difficulty = Sprite("assets/menu/difficulty.png")
    difficulty.y = ranking.y - difficulty.height - 24
    difficulty_hover = Sprite("assets/menu/difficulty-hover.png")

    play = Sprite("assets/menu/play.png")
    play.y = difficulty.y - play.height - 24
    play_hover = Sprite("assets/menu/play-hover.png")

    for element in [play, difficulty, ranking, exit_btn]:
        center_x_in_window(element, window)

    btn_pairs =[(play, play_hover), (difficulty, difficulty_hover), (ranking, ranking_hover), (exit_btn, exit_hover)]
    for pair in btn_pairs:
        pair[1].x = pair[0].x
        pair[1].y = pair[0].y

    while True:
        window.set_background_color([0, 0, 0])

        mouse = window.get_mouse()
        for btn, btn_hover in btn_pairs:
            if mouse.is_over_object(btn):
                btn_hover.draw()
            else:
                btn.draw()

        if mouse.is_over_object(play) and mouse.is_button_pressed(1):
            Game(window)

        if mouse.is_over_object(difficulty) and mouse.is_button_pressed(1):
            Difficulty(window)

        if mouse.is_over_object(exit_btn) and mouse.is_button_pressed(1):
            return

        window.update()


if __name__ == '__main__':
    main()
