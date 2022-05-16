def generate_grammar(approximation, rhs, max_level, depth, samples=37):

    coarsest = False
    if depth == 1:
        coarsest = True
    pset, terminals, types = init_grammar(approximation, rhs, max_level, samples, coarsest=coarsest)

    for i in range(1, depth):
        level = max_level - i
        approximation = system.ZeroApproximation(terminals.coarse_grid)
        operator = terminals.coarse_operator
        if i == depth - 1:
            coarsest = True
        coarse_operator = get_operator(level - 1)
        restriction_operators, prolongation_operators = get_inter_grid_operators(level, level - 1)
        coarse_grid_solver = base.CoarseGridSolver("Coarse-Grid Solver", coarse_operator)
        relaxation_factor_interval = np.linspace(0.1, 1.9, samples)
        terminals = Terminals(approximation, operator, coarse_operator, restriction_operators, prolongation_operators, coarse_grid_solver, relaxation_factor_interval, partitionings)
        previous_types = types
        types = Types(i, previous_types)
        add_level(pset, terminals, types, max_level, i, samples, coarsest=coarsest)

    return pset
