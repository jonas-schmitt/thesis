class OptimizationParameters:
    def __init__(self, max_level, depth, generations, mu_, lambda_):
        self.max_level = max_level
        self.depth = depth
        self.generations = generations
        self.mu_ = mu_
        self.lambda_ = lambda_
        self.initial_population_size = 4 * mu_
        self.crossover_probability = 0.7
        self.relaxation_factor_samples=37
        self.tree_min_height = 10
        self.tree_max_height = 50

class Optimizer:
    def __init__(self, program_generator):
        self.program_generator = program_generator
        self.pset = None
        self.toolbox = None
        self.individual_cache = {}

    def run(self, params, use_random_search=False, multi_objective=True):
        self.pset = generate_grammar(self.program_generator, params.max_level, params.depth, params.relaxation_factor_samples)
        self.init_toolbox(self.pset, params.tree_min_height, params.tree_max_height, multi_objective)
        if multi_objective:
            self.init_multi_objective_selection(self.pset, self.evaluate)
        else:
            self.init_single_objective_selection(self.pset, self.evaluate)
        final_population = self.evolutionary_search(params.initial_population_size, params.generations, params.mu_, params.lambda_, params.crossover_probability, use_random_search)
        return final_population