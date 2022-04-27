def restrict(restriction_operator, cycle):
    return apply(restriction_operator, cycle)

def restrict_and_initiate_cycle(coarse_operator, coarse_approximation, restriction_operator, cycle):
    cycle = restrict(restriction_operator, cycle)
    return initiate_cycle(coarse_operator, coarse_approximation, cycle)

def update_with_coarse_grid_correction(relaxation_factor_index, prolongation_operator, state):
    cycle = coarse_grid_correction(prolongation_operator, state)
    return iterate(relaxation_factor_index, terminals.no_partitioning, cycle)
