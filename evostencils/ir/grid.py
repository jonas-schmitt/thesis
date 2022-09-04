
class Grid:
    def __init__(self, size, spacing, level):
        assert len(size) == len(spacing), 
        "Dimensions of the size and step size must match"
        self._size = size
        self._spacing = spacing
        self._level = level

    @property
    def size(self):
        return self._size

    @property
    def spacing(self):
        return self._spacing

    @property
    def level(self):
        return self._level

    @property
    def dimension(self):
        return len(self.size)
