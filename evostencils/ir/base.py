import abc


class Grid:
    def __init__(self, size, step_size, level):
        assert len(size) == len(step_size), "Dimensions of the size and step size must match"
        self._size = size
        self._step_size = step_size
        self._level = level

    @property
    def size(self):
        return self._size

    @property
    def step_size(self):
        return self._step_size

    @property
    def level(self):
        return self._level

    @property
    def dimension(self):
        return len(self.size)

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.size == other.size and self.step_size == other.step_size


class Expression(abc.ABC):

    @property
    @abc.abstractmethod
    def shape(self):
        pass

    @property
    @abc.abstractmethod
    def grid(self):
        pass


class Entity(Expression):

    @property
    def name(self):
        return self._name

    @property
    def shape(self):
        return self._shape

    @property
    def grid(self):
        return self._grid


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


class BinaryExpression(Expression):

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
