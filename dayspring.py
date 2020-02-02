from time import sleep

from src.display.display import Display

from src.layout.types.fulltime import FullTime

fulltime = FullTime()

while True:
    fulltime.get_content()
    sleep(0.5)
