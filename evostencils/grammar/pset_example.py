from deap import gp
import operator

def generate_grammar(x, y, u, v):
    E = type("E", (object,), {})
    A = type("A", (object,), {})
    B = type("B", (object,), {})
    pset = gp.PrimitiveSetTyped("main", [], ret_type=E)
    # <E> := if <B> then <E> else <E> | <A>
    pset.addPrimitive(lambda b, e1, e2: e1 if b else e2, [B, E, E], E, name="if_then_else")
    pset.addPrimitive(lambda _: _, [A], E, name="id")
    # <A> :=
    pset.addPrimitive(operator.neg, [A], A)         # -<A> |
    pset.addPrimitive(operator.add, [A, A], A)      # <A> + <A> |
    pset.addPrimitive(operator.sub, [A, A], A)      # <A> - <A> |
    pset.addPrimitive(operator.mul, [A, A], A)      # <A> * <A> |
    pset.addPrimitive(operator.truediv, [A, A], A)  # <A> / <A> |
    pset.addPrimitive(operator.pow, [A, A], A)      # <A>^<A>
    # <B> :=
    pset.addPrimitive(operator.not_, [B], B)        # not <B> |
    pset.addPrimitive(operator.and_, [B, B], B)     # <B> and <B> |
    pset.addPrimitive(operator.or_, [B, B], B)      # <B> or <B>

    def add_argument(pset, arg, type_list):
        symbolic = True
        for t in type_list:
            pset._add(gp.Terminal(arg, symbolic, t))
            pset.terms_count += 1
        pset.arguments.append(arg)

    add_argument(pset, x, [E, A])
    add_argument(pset, y, [E, A])
    add_argument(pset, u, [B])
    add_argument(pset, v, [B])
    return pset

pset = generate_grammar("x", "y", "u", "v")
expr = gp.genGrow(pset, 3, 5)
tree = gp.PrimitiveTree(expr)
f = gp.compile(tree, pset)
print(tree)
print(f(42, 7, False, True))
