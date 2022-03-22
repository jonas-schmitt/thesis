class UnaryExpression(Expression):

    def __init__(self, operand):
        self._operand = operand
        self._shape = operand.shape
        super().__init__()

    @property
    def operand(self):
        return self._operand

    @property
    def shape(self):
        return self._shape

    @property
    def grid(self):
        return self.operand.grid
