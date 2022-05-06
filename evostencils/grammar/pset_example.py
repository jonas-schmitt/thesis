from deap import gp
import operator

class E:
    pass

class A:
    pass

class B:
    pass

def add_argument(pset, arg, type_list):
    for t in type_list:
        pset._add(gp.Terminal(arg, True, t))
        pset.terms_count += 1
    pset.arguments.append(arg)

def generate_pset(x, y, u, v):
    pset = gp.PrimitiveSetTyped("main", [], E)
    add_argument(pset, x, [E, A])
    add_argument(pset, y, [E, A])
    add_argument(pset, u, [B])
    add_argument(pset, v, [B])

    def if_then_else(b, e1, e2):
        return e1 if b else e2

    def id(_):
        return _

    # if <B> then <E> else <E> | A
    pset.addPrimitive(if_then_else, [B, E, E], E)
    pset.addPrimitive(id, [A], E)

    pset.addPrimitive(operator.neg, [A], A) # -<A>
    pset.addPrimitive(operator.add, [A, A], A) # <A> + <A>
    pset.addPrimitive(operator.sub, [A, A], A) # <A> - <A>
    pset.addPrimitive(operator.mul, [A, A], A) # <A> * <A>
    pset.addPrimitive(operator.truediv, [A, A], A) # <A> / <A>
    pset.addPrimitive(operator.pow, [A, A], A) # <A>^<A>

    pset.addPrimitive(operator.not_, [B], B) # not <B>
    pset.addPrimitive(operator.and_, [B, B], B) # <B> and <B>
    pset.addPrimitive(operator.or_, [B, B], B) # <B> or <B>
    return pset

pset = generate_pset("x", "y", "u", "v")
expr = gp.genGrow(pset, 3, 5)
tree = gp.PrimitiveTree(expr)
print(tree)
f = gp.compile(tree, pset)
print(f(1,2, True, True))
