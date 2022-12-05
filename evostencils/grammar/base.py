def residual(state):
    x_h, b_h = state
    return base.Cycle(x_h, b_h, base.Residual(terminals.A_h, approximation, rhs), predecessor=approximation.predecessor)

def apply(A_h, cycle):
    cycle.correction = base.Multiplication(A_h, cycle.correction)
    return cycle

def update(relaxation_factor_index, partitioning, cycle):
    relaxation_factor = terminals.relaxation_factor_interval[relaxation_factor_index]
    cycle.relaxation_factor = relaxation_factor
    cycle.partitioning = partitioning
    x_h, b_h = cycle, cycle.rhs
    return x_h, b_h

def coarsening(A_2h, x_2h, cycle):
    r_2h = base.Residual(A_2h, x_2h, cycle.correction)
    new_cycle = base.Cycle(x_2h, cycle.correction, r_2h)
    new_cycle.predecessor = cycle
    return new_cycle

def coarse_grid_correction(P_2h, state):
    cycle = state[0]
    correction = base.Multiplication(P_2h, cycle)
    cycle.predecessor.correction = correction
    return cycle.predecessor
