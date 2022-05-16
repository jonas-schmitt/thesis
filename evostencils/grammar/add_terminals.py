def add_terminals(pset: PrimitiveSetTyped, terminals: Terminals, types: Types, max_level, depth, coarsest=False):
    level = max_level - depth
    if not coarsest:
        coarse_zero_approximation = system.ZeroApproximation(terminals.coarse_grid)
        pset.addTerminal(coarse_zero_approximation, types.x_2h, f'zero_{level - 1}')
        pset.addTerminal(terminals.coarse_operator, types.A_2h, f'A_{level - 1}')
    for prolongation in terminals.prolongation_operators:
        pset.addTerminal(prolongation, types.P_2h, prolongation.name)
    for restriction in terminals.restriction_operators:
        pset.addTerminal(restriction, types.R_h, restriction.name)
