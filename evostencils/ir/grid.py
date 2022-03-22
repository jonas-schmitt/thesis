class Grid:
    def __init__(self, size, step_size, level):
        assert len(size) == len(step_size), 
        "Dimensions of the size and step size must match"
        self._size = size
        self._step_size = step_size
        self._level = level

    @property
    def size(self):
        return self._size

    @property
    def step_size(self):
        return self._step_size

    @property
    def level(self):
        return self._level

    @property
    def dimension(self):
        return len(self.size)
