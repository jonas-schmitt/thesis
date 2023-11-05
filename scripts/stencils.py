import sympy as sp


def add(s1: set, s2: set):
    if len(s2) == 0:
        return s1
    elif len(s1) == 0:
        return s2
    else:
        s1_ = s1.copy()
        s2_ = s2.copy()
        a, b = s1_.pop()
        in_both = False
        c = None
        for x, y in s2:
            if x == a:
                c = y
                in_both = True
                break
        if in_both:
            s2_.remove((a, c))
            return {(a, b + c)} | add(s1_, s2_)
        else:
            return {(a, b)} | add(s1_, s2)


def mult(s1: set, s2: set):
    if len(s1) == 0 or len(s2) == 0:
        return set()
    else:
        s1_ = s1.copy()
        s2_ = s2.copy()
        a, b = s1_.pop()
        c, d = s2_.pop()
        tmp1 = {(a+c, b*d)}
        tmp2 = mult({(a, b)}, s2_)
        tmp3 = mult(s1_, s2)
        return add(add(tmp1, tmp2), tmp3)
        # return tmp1 | tmp2 | tmp3


a1, b1, a2, b2, a3, b3 = sp.symbols("a1, b1, a2, b2, a3, b3")
c1, d1, c2, d2, c3, d3 = sp.symbols("c1, d1, c2, d2, c3, d3")

s1 = {(0, 2), (1, -1), (-1, -1)}
s2 = {(0, 2), (1, -1), (-1, -1)}
# s2 = {(0, 4), (1, -1), (-1, -1), (2, -1), (-2, -1)}
s1_ = s1.copy()
s2_ = s2.copy()
tmp0 = add(s1_, s2_)
s1_ = s1.copy()
s2_ = s2.copy()
tmp1 = mult(s1_, s2_)
s1_ = s1.copy()
s2_ = s2.copy()
tmp2 = mult(s1_, s2_)
print(tmp1 == tmp2)
