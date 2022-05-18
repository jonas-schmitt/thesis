def correct_with_coarse_grid_solver(relaxation_factor_index, P_2h, CGS_2h, R_h, cycle):
    cycle = apply(R_h, cycle)
    cycle = apply(CGS_2h, cycle)
    cycle = apply(P_2h, cycle)
    return update(relaxation_factor_index, terminals.no_partitioning, cycle)
