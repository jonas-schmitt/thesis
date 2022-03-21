import abc
from functools import reduce
from evostencils.expressions import partitioning as part
from evostencils.stencils import periodic, gallery
from evostencils.stencils import constant


# Base classes
class Expression(abc.ABC):
    def __init__(self):
        self.lfa_symbol = None
        self.valid = False
        self.runtime = None

    @property
    @abc.abstractmethod
    def shape(self):
        pass

    @abc.abstractmethod
    def apply(self, transform: callable, *args):
        pass

    @abc.abstractmethod
    def mutate(self, f: callable, *args):
        pass


class Entity(Expression):

    @property
    def name(self):
        return self._name

    @property
    def shape(self):
        return self._shape

    def __str__(self):
        return f'{self.name}'

    def apply(self, _, *args):
        return self

    def mutate(self, f: callable, *args):
        pass


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

    def apply(self, transform: callable, *args):
        return type(self)(transform(self.operand, *args))

    def mutate(self, f: callable, *args):
        f(self.operand, *args)

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

    def apply(self, transform: callable, *args):
        return type(self)(transform(self.operand1, *args), transform(self.operand2, *args))

    def mutate(self, f: callable, *args):
        f(self.operand1, *args)
        f(self.operand2, *args)
