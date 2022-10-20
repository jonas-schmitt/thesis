from operator import mul

class Operator(Entity):
    def __init__(self, name, grid, stencil_generator=None):
        n = reduce(mul, grid.size)
        shape = (n, n)
        self._stencil_generator = stencil_generator
        super().__init__(name, grid, shape)

    @property
    def stencil_generator(self):
        return self._stencil_generator

    def generate_stencil(self):
        if self._stencil_generator is None:
            return None
        return self._stencil_generator.generate_stencil(self._grid)
