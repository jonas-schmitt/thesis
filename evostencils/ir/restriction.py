from operator import mul

class Restriction(InterGridOperator):
    def __init__(self, name, fine_grid, coarse_grid, stencil_generator=None):
        super().__init__(name, coarse_grid, fine_grid, coarse_grid, stencil_generator)
        from functools import reduce
        tmp1 = reduce(mul, fine_grid.size)
        tmp2 = reduce(mul, coarse_grid.size)
        self._shape = (tmp2, tmp1)

    @property
    def fine_grid(self):
        return self._fine_grid

    @property
    def coarse_grid(self):
        return self._coarse_grid
