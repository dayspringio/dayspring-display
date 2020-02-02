from src.layout.tiles.tile import Tile
from src.layout.types.layouttype import LayoutType
from src.updaters.dateupdater import DateUpdater
from src.updaters.timeupdater import TimeUpdater


class FullTime(LayoutType):
    def __init__(self):
        self.name = "Full time"
        self.tiles = [
            Tile([3, 1], [0, 0], None, TimeUpdater()),
            Tile([3, 1], [1, 1], None, DateUpdater()),
        ]
        super().__init__(self.tiles)
