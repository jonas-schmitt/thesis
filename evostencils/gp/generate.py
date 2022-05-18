import random
from inspect import isclass

def generate(pset, min_height, max_height, condition, type_=None):
    if type_ is None:
        type_ = pset.ret
    expression = []
    height = random.randint(min_height, max_height)
    stack = [(0, type_)]
    max_depth = 0
    while len(stack) != 0:
        depth, type_ = stack.pop()
        max_depth = max(max_depth, depth)
        if max_depth > 90:
            return None
        terminals_available = len(pset.terminals[type_]) > 0
        if condition(height, depth):
            nodes = pset.terminals[type_] + pset.primitives[type_]
        else:
            if terminals_available:
                nodes = pset.terminals[type_]
            else:
                nodes = pset.primitives[type_]
        if len(nodes) == 0:
            raise RuntimeError(f"Neither terminal nor primitive available for {type_}")
        choice = random.choice(nodes)
        if choice.arity > 0:
            for arg in reversed(choice.args):
                stack.append((depth + 1, arg))
        else:
            if isclass(choice):
                choice = choice()
        expression.append(choice)
    return expression
