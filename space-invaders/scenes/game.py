from vendor.pplay.sprite import Sprite
from vendor.pplay.window import Window

from core.fps import FPS


def clamp(value, min_v, max_v): return max(min(value, max_v), min_v)


class EnemyGrid:
    _window: Window

    _enemies: list[list[Sprite]]
    _enemy_size = [40, 30]
    _enemy_speed = 0.125
    _enemy_direction = 1

    def __init__(self, window: Window, size_x: int = 5, size_y: int = 3):
        self._window = window
        self._enemies = []

        for y in range(size_y):
            row = []
            pos_y = 32 + (self._enemy_size[1] * y) + (self._enemy_size[1] * 0.5 * y)
            for x in range(size_x):
                pos_x = 32 + (self._enemy_size[0] * x) + (self._enemy_size[0] * 0.5 * x)
                enemy = Sprite("assets/actors/alien.png")
                enemy.set_position(pos_x, pos_y)
                row.append(enemy)

            self._enemies.append(row)

    def draw(self):
        for enemy_row in self._enemies:
            for enemy in enemy_row:
                enemy.move_x(self._enemy_speed * self._enemy_direction)
                if enemy.x + enemy.width >= self._window.width - 32 or enemy.x < 32:
                    self.jump_down()

                enemy.draw()

    def get_max_y(self):
        return self._enemies[len(self._enemies) - 1][0].y + self._enemy_size[1]

    def jump_down(self):
        self._enemy_direction *= -1
        for row in self._enemies:
            for enemy in row:
                enemy.y += enemy.height + (enemy.height * 0.5)


def GameOver(window: Window):
    _duration = 0

    while True:
        _duration += window.delta_time()

        if _duration > 3:
            return

        window.set_background_color([0, 0, 0])
        window.draw_text("Game over", window.width / 2 - 60, window.height / 2 - 32, 32, [255, 255, 255])
        window.update()


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
