def update_with_exact_coarse_grid_correction(relaxation_factor_index, prolongation_operator, coarse_grid_solver, cycle):
    cycle = apply(prolongation_operator, apply(coarse_grid_solver, cycle))
    return iterate(relaxation_factor_index, terminals.no_partitioning, cycle)

def prolongate_solve_restrict(relaxation_factor_index, prolongation_operator, coarse_grid_solver, restriction_operator, cycle):
    cycle = restrict(restriction_operator, cycle)
    return update_with_exact_coarse_grid_correction(relaxation_factor_index, prolongation_operator, coarse_grid_solver, cycle)
