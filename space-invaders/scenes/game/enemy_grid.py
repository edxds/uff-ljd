from vendor.pplay.sprite import Sprite
from vendor.pplay.window import Window


class EnemyGrid:
    _window: Window

    _enemies: list[list[Sprite]]
    _enemy_size = [40, 30]
    _enemy_speed = 0.125
    _enemy_direction = 1

    def __init__(self, window: Window, size_x: int = 11, size_y: int = 5):
        self._window = window
        self._enemies = []

        for y in range(size_y):
            row = []
            pos_y = 48 + (self._enemy_size[1] * y) + (self._enemy_size[1] * 0.5 * y)
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

    def process_shots(self, shots: list[Sprite]) -> list[Sprite]:
        shots_to_remove = []

        for shot in shots:
            if shot.y > self.get_max_y():
                continue

            collided = self._check_shot_collision(shot)
            if collided:
                shots_to_remove.append(shot)

        return shots_to_remove

    def get_max_y(self):
        return self._enemies[len(self._enemies) - 1][0].y + self._enemy_size[1]

    def jump_down(self):
        self._enemy_direction *= -1
        for row in self._enemies:
            for enemy in row:
                enemy.y += enemy.height + (enemy.height * 0.5)

    def _check_shot_collision(self, shot: Sprite) -> bool:
        for row in self._enemies:
            for enemy in row:
                if shot.collided(enemy):
                    row.remove(enemy)
                    if len(row) == 0:
                        self._enemies.remove(row)
                    return True
