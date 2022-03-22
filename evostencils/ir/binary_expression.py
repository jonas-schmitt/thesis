class BinaryExpression(Expression):

    def __init__(self, operand1, operand2):
        self._operand1 = operand1
        self._operand2 = operand2
        super().__init__()

    @property
    def operand1(self):
        return self._operand1

    @property
    def operand2(self):
        return self._operand2

    @property
    def shape(self):
        return self._shape

    @property
    def grid(self):
        return self.operand1.grid
