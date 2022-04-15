class Cycle(Expression):
    def __init__(self, approximation, rhs, correction=None, relaxation_factor=1.0, partitioning=None, predecessor=None):
        self.approximation = approximation
        self.rhs = rhs
        self.correction = correction
        self.relaxation_factor = relaxation_factor
        self.partitioning = partitioning
        self.predecessor = predecessor
        super().__init__()

    @property
    def shape(self):
        return self.approximation.shape

    @property
    def grid(self):
        return self.approximation.grid
