def coarse_cycle(coarse_approximation, cycle):
    tmp = Cycle(coarse_approximation, cycle.correction, Residual(terminals.coarse_operator, coarse_approximation, cycle.correction))
    cycle.correction = tmp
    cycle.correction.predecessor = cycle
    return cycle.correction

def coarse_grid_correction(relaxation_factor_index, interpolation, state):
    cycle = state[0]
    correction = base.Multiplication(interpolation, cycle)
    cycle.predecessor.correction = correction
    return iterate(relaxation_factor_index, terminals.no_partitioning, cycle.predecessor)

