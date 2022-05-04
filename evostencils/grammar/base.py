def residual(state):
    approximation, rhs = state
    return base.Cycle(approximation, rhs, base.Residual(terminals.operator, approximation, rhs), predecessor=approximation.predecessor)

def apply(operator, cycle):
    cycle.correction = base.Multiplication(operator, cycle.correction)
    return cycle

def update(relaxation_factor_index, partitioning, cycle):
    relaxation_factor = terminals.relaxation_factor_interval[relaxation_factor_index]
    cycle.relaxation_factor = relaxation_factor
    cycle.partitioning = partitioning
    approximation, rhs = cycle, cycle.rhs
    return approximation, rhs

def initiate_cycle(coarse_operator, coarse_approximation, cycle):
    coarse_residual = base.Residual(coarse_operator, coarse_approximation, cycle.correction)
    new_cycle = base.Cycle(coarse_approximation, cycle.correction, coarse_residual)
    new_cycle.predecessor = cycle
    return new_cycle

def coarse_grid_correction(prolongation_operator, state):
    cycle = state[0]
    correction = base.Multiplication(prolongation_operator, cycle)
    cycle.predecessor.correction = correction
    return cycle.predecessor
