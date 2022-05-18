from evostencils.ir import partitioning

class Terminals:
    def __init__(self, x_h, A_h, A_2h, restriction_operators, prolongation_operators, CGS_2h, relaxation_factor_interval, partitionings=None):
        self.A_h = A_h
        self.A_2h = A_2h
        self.x_h = x_h
        self.prolongation_operators = prolongation_operators
        self.restriction_operators = restriction_operators
        self.CGS_2h = CGS_2h
        self.relaxation_factor_interval = relaxation_factor_interval
        self.no_partitioning = partitioning.Single
        self.partitionings = partitionings

    @property
    def grid(self):
        return self.A_h.grid

    @property
    def coarse_grid(self):
        return self.A_2h.grid
