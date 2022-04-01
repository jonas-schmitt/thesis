class Iteration(Expression):
    def __init__(self, approximation, rhs, correction, partitioning=None,
                 relaxation_factor=1.0, predecessor=None):
        self.approximation = approximation
        self.rhs = rhs
        self.correction = correction
        self.relaxation_factor = relaxation_factor
        self.partitioning = partitioning
        self.predecessor = predecessor
        super().__init__()

    @property
    def shape(self):
        return self._approximation.shape

    @property
    def grid(self):
        return self.approximation.grid
