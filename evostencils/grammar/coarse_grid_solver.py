def exact_coarse_grid_correction_iteration(relaxation_factor_index, prolongation_operator, coarse_grid_solver, cycle):
    cycle = apply(prolongation_operator, apply(coarse_grid_solver, cycle))
    return iterate(relaxation_factor_index, terminals.no_partitioning, cycle)

def restrict_solve_prolongate(relaxation_factor_index, prolongation_operator, coarse_grid_solver, restriction_operator, cycle):
    cycle = apply(restriction_operator, cycle)
    return exact_coarse_grid_correction_iteration(relaxation_factor_index, prolongation_operator, coarse_grid_solver, cycle)
