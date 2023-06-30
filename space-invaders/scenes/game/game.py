from vendor.pplay.sprite import Sprite
from vendor.pplay.window import Window

from core.fps import FPS

from .enemy_grid import EnemyGrid
from .game_over import GameOver
from .player import Player


def Game(window: Window):
    keyboard = window.get_keyboard()
    fps = FPS(window)

    player = Player(window)
    enemy_grid = EnemyGrid(window)
    score = 0

    while True:
        fps.tick()
        window.set_background_color([0, 0, 0])

        if enemy_grid.get_max_y() >= player.y:
            GameOver(window)
            return

        if keyboard.key_pressed("ESC"):
            return

        fps.draw()

        shots_to_remove = enemy_grid.process_shots(player.get_shots())
        score += len(shots_to_remove) * 10
        for shot in shots_to_remove:
            player.destroy_shot(shot)

        player.draw()
        enemy_grid.draw()
        window.draw_text(f"Pontos: {score}", window.width / 2 - 50, 16, 16, [255, 255, 255])

        window.update()
