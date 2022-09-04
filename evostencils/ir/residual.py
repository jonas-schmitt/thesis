class Residual(Expression):
    def __init__(self, operator, approximation, rhs):
        self._operator = operator
        self._approximation = approximation
        self._rhs = rhs
        super().__init__()

    @property
    def shape(self):
        return self.rhs.shape

    @property
    def grid(self):
        return self.rhs.grid

    @property
    def operator(self):
        return self._operator

    @property
    def approximation(self):
        return self._approximation

    @property
    def rhs(self):
        return self._rhs
