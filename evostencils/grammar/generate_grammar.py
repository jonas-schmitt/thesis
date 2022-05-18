import numpy as np

def generate_grammar(x_h, rhs, max_level, depth, samples=37):

    coarsest = False
    if depth == 1:
        coarsest = True
    pset, terminals, types = init_grammar(x_h, rhs, max_level, samples, coarsest=coarsest)

    for i in range(1, depth):
        level = max_level - i
        x_h = Approximation(terminals.coarse_grid)
        A_h = terminals.A_2h
        if i == depth - 1:
            coarsest = True
        A_2h = get_operator(level - 1)
        restriction_operators, prolongation_operators = get_inter_grid_operators(level, level - 1)
        CGS_2h = CoarseGridSolver("CGS", A_2h)
        relaxation_factor_interval = np.linspace(0.1, 1.9, samples)
        terminals = Terminals(x_h, A_h, A_2h, restriction_operators, prolongation_operators, CGS_2h, relaxation_factor_interval, partitionings)
        previous_types = types
        types = Types(i, previous_types)
        add_level(pset, terminals, types, max_level, i, samples, coarsest=coarsest)

    return pset
