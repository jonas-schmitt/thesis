from operator import mul

class Approximation(Entity):
    def __init__(self, name, grid):
        shape = (reduce(operator.mul, grid.size), 1)
        super().__init__(name, grid, shape)

    @property
    def grid(self):
        return self._grid

    @property
    def dimension(self):
        return len(self.grid.dimension)


class RightHandSide(Approximation):
    pass
