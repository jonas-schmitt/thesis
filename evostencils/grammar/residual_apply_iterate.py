def residual(state):
    approximation, rhs = state
    return base.Cycle(approximation, rhs, base.Residual(terminals.operator, approximation, rhs), predecessor=approximation.predecessor)

def apply(operator, cycle):
    cycle.correction = base.Multiplication(operator, cycle.correction)
    return cycle

def iterate(relaxation_factor_index, partitioning, cycle):
    relaxation_factor = terminals.relaxation_factor_interval[relaxation_factor_index]
    rhs = cycle.rhs
    cycle.relaxation_factor = relaxation_factor
    cycle.partitioning = partitioning
    approximation = cycle
    return approximation, rhs
