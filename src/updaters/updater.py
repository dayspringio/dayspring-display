import time
import logging

class Updater:
    def __init__(self, update_interval=1):
        self.logger = logging.getLogger('root')
        self.time = time
        self.update_interval = update_interval
        self.custom_interval = 0
        self.last_execution = 0

    def update(self):
        print("Updating")
        self.last_execution = time.time()

    def check_updater(self):
        interval = self.custom_interval if self.custom_interval != 0 else self.update_interval
        print("Interval check", self.time.time() - self.last_execution, interval)
        if self.time.time() - self.last_execution > interval:
            # Reset custom interval just in case
            self.custom_interval = 0
            return True
        return False
