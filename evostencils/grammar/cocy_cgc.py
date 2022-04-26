def coarse_cycle(coarse_approximation, cycle):
    coarse_residual = base.Residual(terminals.coarse_operator, coarse_approximation, cycle.correction)
    new_cycle = base.Cycle(coarse_approximation, cycle.correction, coarse_residual)
    new_cycle.predecessor = cycle
    return new_cycle

def coarse_grid_correction(prolongation_operator, state):
    cycle = state[0]
    predecessor = cycle.predecessor
    predecessor.correction = base.Multiplication(prolongation_operator, cycle)
    return predecessor

