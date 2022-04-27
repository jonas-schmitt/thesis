def generate_jacobi(operator: base.Operator):
    return base.Diagonal(operator)

def jacobi(relaxation_factor_index, partitioning, cycle):
    return smoothing(relaxation_factor_index, partitioning, generate_jacobi, cycle)
