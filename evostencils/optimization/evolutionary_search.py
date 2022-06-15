def evolutionary_search(self, params, use_random_search=False):
    # Generate and evaluate initial population
    population = self.toolbox.population(n=params.initial_population_size)
    invalid_ind = [ind for ind in population]
    self.evaluate_individuals(invalid_ind)
    # Select mu individuals from the initial population
    population = self.toolbox.select(population, params.mu_)
    for gen in range(1, params.generations + 1):
        if use_random_search:
            # For random search simply generate individuals randomly
            offspring = self.toolbox.population(n=params.lambda_)
        else:
            # Select lambda parents for mutation and crossover
            selected = self.toolbox.select(population, params.lambda_)
            parents = [self.toolbox.clone(ind) for ind in selected]
            offspring = self.create_offspring(parents, params.crossover_probability)
        # Evaluate new individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        self.evaluate_individuals(invalid_ind)
        # Select new population from the combined set of parents
        # and offspring (elitism)
        population = self.toolbox.elitism(population + offspring, params.mu_)

    return population