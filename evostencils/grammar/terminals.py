class Terminals:
    def __init__(self, approximation, operator, coarse_operator, restriction, prolongation, coarse_grid_solver_expression=None):
        self.approximation = approximation
        self.operator = operator
        self.coarse_operator = coarse_operator
        self.prolongation = prolongation
        self.restriction = restriction
        self.coarse_grid_solver = base.CoarseGridSolver(self.coarse_operator, expression=coarse_grid_solver_expression)
        self.no_partitioning = part.Single
        self.red_black_partitioning = part.RedBlack

    @property
    def grid(self):
        return self.operator.grid

    @property
    def coarse_grid(self):
        return self.coarse_operator.grid
