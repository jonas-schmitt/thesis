class Optimizer:
    def __init__(self, program_generator):
        self.program_generator = program_generator
        self.pset = None
        self.toolbox = None
        self.params = None
        self.individual_cache = {}

    def run(self, params, use_random_search=False):
        self.params = params
        self.pset = generate_grammar(self.program_generator, params.max_level, params.depth, params.relaxation_factor_samples)
        min_level = params.max_level - params.depth
        self.program_generator.initialize_code_generation(min_level, params.max_level)
        self.init_toolbox(self.pset, params.tree_min_height, params.tree_max_height, params.multi_objective)
        if params.multi_objective:
            self.init_multi_objective_selection(self.pset, self.evaluate)
        else:
            self.init_single_objective_selection(self.pset, self.evaluate)
        final_population = self.evolutionary_search(params, use_random_search)
        return final_population
