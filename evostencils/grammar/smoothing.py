def smoothing(relaxation_factor_index, partitioning, generate_smoother, cycle):
    assert isinstance(cycle.correction, base.Residual), 'Invalid production: expected residual'
    smoothing_operator = generate_smoother(cycle.correction.operator)
    cycle = apply(base.Inverse(smoothing_operator), cycle)
    return update(relaxation_factor_index, partitioning, cycle)
