import random
from inspect import isclass

def generate(pset, min_height, max_height, condition, return_type=None, subtree=None):
    if return_type is None:
        type_ = pset.ret
    else:
        type_ = return_type
    expression = []
    height = random.randint(min_height, max_height)
    stack = [(0, type_)]
    max_depth = 0
    subtree_inserted = False
    if subtree is None:
        subtree_inserted = True
    while len(stack) != 0:
        depth, type_ = stack.pop()
        if not subtree_inserted and type_ == return_type and len(expression) > 0:
            expression.extend(subtree)
            subtree_inserted = True
            continue
        max_depth = max(max_depth, depth)
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
