from __future__ import annotations

from vendor.pplay.sprite import Sprite
from vendor.pplay.window import Window


def clamp(value, min_v, max_v): return max(min(value, max_v), min_v)


class Player(Sprite):
    _shots: list[Sprite] = []
    _shoot_cooldown = 500
    _last_shot_timestamp = 0

    def __init__(self, window: Window):
        super().__init__("assets/actors/player.png")
        self._window = window
        self.set_position(window.width / 2 - self.width / 2, window.height - self.height - 32)

    def draw(self):
        self._move_on_input()
        self._shoot_on_input()
        self._draw_shots()
        super().draw()

    def get_shots(self):
        return self._shots

    def destroy_shot(self, shot: Sprite):
        self._shots.remove(shot)

    def _move_on_input(self):
        self.move_key_x(0.8)
        self.x = clamp(self.x, 0, self._window.width - self.width)

    def _shoot_on_input(self):
        keyboard = self._window.get_keyboard()
        if not keyboard.key_pressed("space"):
            return

        time_since_last_shot = self._window.curr_time - self._last_shot_timestamp
        if self._last_shot_timestamp != 0 and time_since_last_shot < self._shoot_cooldown:
            return

        shot = Sprite("assets/actors/shoot.png")
        shot.x = self.x + self.width / 2 - shot.width / 2
        shot.y = self.y - 4

        self._last_shot_timestamp = self._window.curr_time
        self._shots.append(shot)

    def _draw_shots(self):
        for shot in self._shots:
            shot.move_y(-0.8)
            shot.draw()
