from functools import reduce

from vendor.pplay.window import Window


class FPS:
    _records: list[int] = []

    _time_since_last_record = 0
    _ticker = 0

    def __init__(self, window: Window, interval=3):
        self._window = window
        self._interval = interval

    def draw(self):
        self._window.draw_text(f"FPS: {self.get_average()}", 4, 4, 12, [255, 255, 255])

    def tick(self):
        self._ticker += 1
        self._time_since_last_record += self._window.delta_time()
        if self._time_since_last_record < 1:
            return

        if len(self._records) == self._interval:
            self._records.clear()

        self._records.append(self._ticker)
        self._time_since_last_record = 0
        self._ticker = 0

    def get_average(self):
        if len(self._records) == 0:
            return 0

        return round(reduce(lambda x, y: x + y, self._records) / len(self._records))
