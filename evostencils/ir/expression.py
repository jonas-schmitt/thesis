import abc

class Expression(abc.ABC):

    @property
    @abc.abstractmethod
    def shape(self):
        pass

    @property
    @abc.abstractmethod
    def grid(self):
        pass
