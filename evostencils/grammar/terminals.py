class Terminals:
    def __init__(self, approximation, coarsening_factors, operator, coarse_operator, restriction, prolongation,
                 coarse_grid_solver_expression=None):
        self.grid = approximation.grid
        self.coarse_grid = system.get_coarse_grid(self.grid, coarsening_factors)
        self.operator = operator
        self.approximation = approximation
        self.prolongation = prolongation
        self.restriction = restriction
        self.coarse_operator = coarse_operator
        self.coarse_grid_solver = base.CoarseGridSolver(self.coarse_operator, expression=coarse_grid_solver_expression)
        self.no_partitioning = part.Single
        self.red_black_partitioning = part.RedBlack
