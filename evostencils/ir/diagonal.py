import evostencils.stencils as stencils

class Diagonal(UnaryExpression):
    def generate_stencil(self):
        return stencils.multiple.diagonal(self.operand.generate_stencil())


class BlockDiagonal(UnaryExpression):
    def __init__(self, operand, block_size):
        self._block_size = block_size
        super().__init__(operand)

    def generate_stencil(self):
        operand_stencil = self.operand.generate_stencil()
        return stencils.multiple.block_diagonal(operand_stencil, self.block_size)

    @property
    def block_size(self):
        return self._block_size
