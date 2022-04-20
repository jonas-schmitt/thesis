def residual(state):
    return Cycle(state[0], state[1], Residual(terminals.operator, state[0], state[1]), predecessor=state[0].predecessor)

def apply(operator, cycle):
    cycle.correction = Multiplication(operator, cycle.correction)
    return cycle

def iterate(relaxation_factor_index, partitioning, cycle):
    relaxation_factor = relaxation_factor_interval[relaxation_factor_index]
    rhs = cycle.rhs
    cycle.relaxation_factor = relaxation_factor
    cycle.partitioning = partitioning
    approximation = cycle
    return approximation, rhs
