def adapt_problem_size(max_level, depth, tree_min_height, tree_max_height, relaxation_factor_samples, multi_objective=True):
    self.pset = generate_grammar(self.program_generator, max_level, depth, relaxation_factor_samples)
    self.program_generator.initialize_code_generation(max_level-depth, max_level)
    self.init_toolbox(self.pset, tree_min_height, tree_max_height, multi_objective)
    if multi_objective:
        self.init_multi_objective_selection(self.pset, self.evaluate)
    else:
        self.init_single_objective_selection(self.pset, self.evaluate)