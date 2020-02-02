import time

from src.updaters.updater import Updater


class TimeUpdater(Updater):
    def __init__(self):
        super().__init__(1)
        self.content = 0
        self.update()

    def update(self):
        self.content = time.strftime("%H:%M:%S", time.gmtime())
        super().update()

    def get_content(self):
        if self.check_updater():
            self.update()
        return str(self.content)
