from operator import mul

class Approximation(Entity):
    def __init__(self, name, grid):
        shape = (reduce(operator.mul, grid.size), 1)
        super().__init__(name, grid, shape)

    @property
    def predecessor(self):
        return None

class RightHandSide(Approximation):
    pass
