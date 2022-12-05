def restrict_and_coarsen(A_2h, x_2h, R_h, cycle):
    cycle = apply(R_h, cycle)
    return coarsening(A_2h, x_2h, cycle)

def update_with_coarse_grid_correction(relaxation_factor_index, P_2h, state):
    cycle = coarse_grid_correction(P_2h, state)
    return update(relaxation_factor_index, terminals.no_partitioning, cycle)
