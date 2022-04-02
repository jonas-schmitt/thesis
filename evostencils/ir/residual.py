class Residual(Expression):
    def __init__(self, operator, approximation, rhs):
        self.operator = operator
        self.approximation = approximation
        self.rhs = rhs
        super().__init__()

    @property
    def shape(self):
        return self.rhs.shape

    @property
    def grid(self):
        return self.rhs.grid
