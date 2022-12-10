def adapt_problem_size(max_level, params, multi_objective=True):
    self.pset = generate_grammar(self.program_generator, max_level, params.depth, params.relaxation_factor_samples)
    # Initialize the code generator 
    # according to the specified maximum level
    self.program_generator.initialize_code_generation(max_level-params.depth, max_level)
    self.init_toolbox(self.pset, params.tree_min_height, params.tree_max_height, multi_objective)
    if multi_objective:
        self.init_multi_objective_selection(self.pset, self.evaluate)
    else:
        self.init_single_objective_selection(self.pset, self.evaluate)
