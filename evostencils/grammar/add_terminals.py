def add_terminals(pset, terminals, types, max_level, depth, coarsest=False):
    level = max_level - depth
    if not coarsest:
        x_2h = Approximation(terminals.coarse_grid)
        pset.addTerminal(x_2h, types.x_2h, f'zero_{level - 1}')
        pset.addTerminal(terminals.A_2h, types.A_2h, f'A_{level - 1}')
    for P_2h in terminals.prolongation_operators:
        pset.addTerminal(P_2h, types.P_2h, P_2h.name)
    for R_h in terminals.restriction_operators:
        pset.addTerminal(R_h, types.R_h, R_h.name)
