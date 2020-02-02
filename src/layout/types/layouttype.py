class LayoutType:

    def __init__(self, tiles):
        self.tiles = tiles

    def get_content(self):
        # Loop through tiles and get their updated content
        # Call tile update async so it can check and then renew the content as it comes through
        i = 0
        content = ""
        while i < len(self.tiles):
            print(self.tiles[i].get_content())
            content + self.tiles[i].get_content()
            i += 1
        return True
