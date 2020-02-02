from src.layout.tiles.tile import Tile
from src.layout.types.layouttype import LayoutType
from src.updaters.dateupdater import DateUpdater
from src.updaters.timeupdater import TimeUpdater
from src.updaters.weatherupdater import WeatherUpdater


class FullTime(LayoutType):
    def __init__(self):
        self.name = "Full time"
        self.tiles = [
            Tile([3, 1], [0, 0], None, TimeUpdater()),
            Tile([3, 1], [1, 1], None, DateUpdater()),
            Tile([3, 1], [1, 1], None, WeatherUpdater('temperature')),
        ]
        super().__init__(self.tiles)
