import time


class Tile:
    def __init__(self, size, position, tile_content=None, updater=None):
        self.time = time
        self.size = size
        self.position = position
        if updater is None and tile_content is None:
            raise TypeError("'updater' or 'tile_content' MUST be defined")
        if updater:
            self.updater = updater
        if tile_content:
            self.tile_content = tile_content

    def get_content(self):
        if self.updater is not None:
            return self.updater.get_content()
        else:
            return self.tile_content
