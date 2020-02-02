import time


class Updater:
    def __init__(self, update_interval=1):
        self.time = time
        self.update_interval = update_interval
        self.last_execution = 0

    def update(self):
        self.last_execution = time.time()

    def check_updater(self):
        return self.time.time() - self.last_execution > self.update_interval
