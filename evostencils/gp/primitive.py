class Primitive(object):
    def __init__(self, name, args, ret):
        self.name = name # name as a string
        self.arity = len(args)
        self.args = args # list of argument types
        self.ret = ret # return type

class Terminal(object):
    def __init__(self, terminal, symbolic, ret):
        self.ret = ret # return type
        self.value = terminal
        self.name = str(terminal) # name as a string
        self.conv_fct = str if symbolic else repr

    @property
    def arity(self):
        return 0
