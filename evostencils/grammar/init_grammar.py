def init_grammar(approximation, rhs, max_level, samples, coarsest=False):
    operator = get_operator(max_level)
    restriction_operators, prolongation_operators = get_inter_grid_operators(max_level, max_level - 1)
    coarse_operator = get_operator(max_level - 1)
    partitionings = [part.RedBlack]
    coarse_grid_solver = base.CoarseGridSolver("Coarse-Grid Solver", coarse_operator)

    relaxation_factor_interval = np.linspace(0.1, 1.9, samples)
    terminals = Terminals(approximation, operator, coarse_operator, restriction_operators, prolongation_operators, coarse_grid_solver, relaxation_factor_interval, partitionings)
    types = Types(0)
    pset = PrimitiveSetTyped("main", [], types.S_h)
    pset.addTerminal((approximation, rhs), types.S_guard_h, 'initial_state')

    pset.addTerminal(terminals.no_partitioning, types.Partitioning, terminals.no_partitioning.get_name())
    for p in terminals.partitionings:
        pset.addTerminal(p, types.Partitioning, p.get_name())
    for i in range(0, samples):
        pset.addTerminal(i, types.RelaxationFactorIndex)

    add_level(pset, terminals, types, max_level, 0, samples, coarsest=coarsest)
    return pset, terminals, types
