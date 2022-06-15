import random

def evolutionary_search(self, params, use_random_search=False, generalization_interval=None):
    if generalization_interval is None:
        generalization_interval = params.generations
    # Generate and evaluate initial population
    n = params.initial_population_size / self.nprocs
    population = self.toolbox.population(n)
    invalid_ind = [ind for ind in population]
    self.evaluate_individuals(invalid_ind)
    population = self.allgather(population)
    # Select mu individuals from the initial population
    population = self.toolbox.select(population, params.mu_)
    max_level = params.max_level
    for gen in range(1, params.generations + 1):
        if gen > 1 and gen % generalization_interval == 0:
            # Increase the problem size
            max_level += 1
            self.adapt_problem_size(max_level, params, params.multi_objective)
            # Reevaluate individuals
            invalid_ind = [ind for ind in population]
            self.evaluate_individuals(invalid_ind)
        lambda_ = params.lambda_ / self.nprocs
        if use_random_search:
            # For random search simply generate individuals randomly
            offspring = self.toolbox.population(n=lambda_)
        else:
            # Select lambda parents for mutation and crossover
            selected = self.toolbox.select(population, lambda_)
            parents = [self.toolbox.clone(ind) for ind in selected]
            offspring = self.create_offspring(parents, params.crossover_probability)
        # Evaluate new individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        self.evaluate_individuals(invalid_ind)
        offspring = self.allgather(offspring)
        # Select new population from the combined set of parents
        # and offspring (elitism)
        population = self.toolbox.elitism(population + offspring, params.mu_)

    return population