class Entity(Expression):

    def __init__(self, name, grid, shape):
        self._name = name
        self._grid = grid
        self._shape = shape
        super().__init__()

    @property
    def name(self):
        return self._name

    @property
    def grid(self):
        return self._grid

    @property
    def shape(self):
        return self._shape
