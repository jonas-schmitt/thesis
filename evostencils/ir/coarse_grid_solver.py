class CoarseGridSolver(Entity):
    def __init__(self, name, operator, expression=None):
        shape = operator.shape
        self._operator = operator
        self._expression = expression
        super().__init__(name, operator.grid, shape)

    @property
    def operator(self):
        return self._operator

    @property
    def expression(self):
        return self._expression
