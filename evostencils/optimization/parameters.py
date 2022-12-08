class Parameters:
    def __init__(self, max_level, depth, generations, mu_, lambda_):
        self.max_level = max_level
        self.depth = depth
        self.generations = generations
        self.mu_ = mu_
        self.lambda_ = lambda_
        self.initial_population_size = 4 * mu_
        self.crossover_probability = 0.7
        self.relaxation_factor_samples = 37
        self.tree_min_height = 10
        self.tree_max_height = 50
        self.multi_objective = True
