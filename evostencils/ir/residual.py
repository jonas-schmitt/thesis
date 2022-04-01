class Residual(Expression):
    def __init__(self, operator, approximation, rhs):
        # assert iterate.shape == rhs.shape, "Shapes of iterate and rhs must match"
        self.operator = operator
        self.approximation = approximation
        self.rhs = rhs
        super().__init__()

    @property
    def shape(self):
        return self.approximation.shape

    @property
    def grid(self):
        return self.approximation.grid
