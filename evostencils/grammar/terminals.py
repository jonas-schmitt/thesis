from evostencils.ir import partitioning as part

class Terminals:
    def __init__(self, approximation, operator, coarse_operator, restriction_operators, prolongation_operators, coarse_grid_solver, partitionings=None):
        self.operator = operator
        self.coarse_operator = coarse_operator
        self.approximation = approximation
        self.prolongation_operators = prolongation_operators
        self.restriction_operators = restriction_operators
        self.coarse_grid_solver = coarse_grid_solver
        self.no_partitioning = part.Single
        self.partitionings = partitionings

    @property
    def grid(self):
        return self.operator.grid

    @property
    def coarse_grid(self):
        return self.coarse_operator.grid
