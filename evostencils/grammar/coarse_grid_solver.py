def correct_with_coarse_grid_solver(relaxation_factor_index, prolongation_operator, coarse_grid_solver, restriction_operator, cycle):
    cycle = apply(restriction_operator, cycle)
    cycle = apply(coarse_grid_solver, cycle)
    cycle = apply(prolongation_operator, cycle)
    return update(relaxation_factor_index, terminals.no_partitioning, cycle)
