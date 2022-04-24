import evostencils.stencils as stencils

class Multiplication(BinaryExpression):

    def __init__(self, operand1, operand2):
        assert operand1.shape[1] == operand2.shape[0], "Operand shapes are not aligned"
        self._shape = (operand1.shape[0], operand2.shape[1])
        super().__init__(operand1, operand2)

    @property
    def grid(self):
        return self.operand1.grid

    @property
    def shape(self):
        return self._shape
