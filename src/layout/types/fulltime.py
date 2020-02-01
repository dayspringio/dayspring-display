from src.layout.types.layouttype import LayoutType


class FullTime(LayoutType):
    def __init__(self, tiles):
        super().__init__(tiles)
        self.name = "Full time"
        self.tiles = tiles
