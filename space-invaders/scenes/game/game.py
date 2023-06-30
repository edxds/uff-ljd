from vendor.pplay.sprite import Sprite
from vendor.pplay.window import Window

from core.fps import FPS

from .enemy_grid import EnemyGrid
from .game_over import GameOver


def clamp(value, min_v, max_v): return max(min(value, max_v), min_v)


def Game(window: Window):
    keyboard = window.get_keyboard()
    fps = FPS(window)

    player = Sprite("assets/actors/player.png")
    player.set_position(window.width / 2 - player.width / 2, window.height - player.height - 32)

    enemy_grid = EnemyGrid(window)

    while True:
        fps.tick()
        window.set_background_color([0, 0, 0])

        player.move_key_x(0.8)
        player.x = clamp(player.x, 0, window.width - player.width)

        if enemy_grid.get_max_y() >= player.y:
            GameOver(window)
            return

        if keyboard.key_pressed("ESC"):
            return

        fps.draw()

        player.draw()
        enemy_grid.draw()

        window.update()
