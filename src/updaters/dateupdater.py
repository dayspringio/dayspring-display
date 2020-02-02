import time

from src.updaters.updater import Updater


class DateUpdater(Updater):
    def __init__(self):
        super().__init__(1)
        self.content = 0
        self.date_execution = 0
        self.update()

    def update(self):
        gmt_time = time.gmtime()
        # If the current day is not the same as the day it was last executed
        if self.date_execution == 0 or time.strftime("%d", self.date_execution) != time.strftime("%d", gmt_time):
            self.content = time.strftime("%d-%M-%Y", time.gmtime())
            self.date_execution = time.gmtime()

    def check_updater(self):
        return self.last_execution

    def get_content(self):
        # Since we don't use a normal time check we don't use the parent checker
        self.update()
        return str(self.content)
