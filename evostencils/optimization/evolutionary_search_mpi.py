import random

def evolutionary_search(self, params, generalization_interval=None):
    if generalization_interval is None:
        generalization_interval = params.generations
    # Generate and evaluate initial population
    n = params.initial_population_size / self.nprocs
    population = self.toolbox.population(n)
    invalid_ind = [ind for ind in population]
    fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit
    population = self.allgather(population)
    # Select mu individuals from the initial population
    population = self.toolbox.select(population, params.mu_)
    max_level = params.max_level
    for gen in range(1, params.generations + 1):
        if gen > 1 and gen % generalization_interval == 0:
            max_level += 1
            self.adapt_problem_size(max_level, params, multi_objective=True)
        # Select lambda parents for mutation and crossover
        lambda_ = params.lambda_ / self.nprocs
        selected = self.toolbox.select(population, lambda_)
        parents = [self.toolbox.clone(ind) for ind in selected]
        offspring = []
        for ind1, ind2 in zip(parents[::2], parents[1::2]):
            operator_choice = random.random()
            if operator_choice < params.crossover_probability:
                child1, child2 = self.toolbox.mate(ind1, ind2)
            else:
                child1, = self.toolbox.mutate(ind1)
                child2, = self.toolbox.mutate(ind2)
            del child1.fitness.values, child2.fitness.values
            offspring.extend([child1, child2])
        # Evaluate new individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        offspring = self.allgather(offspring)
        # Select new population from the combined set of parents
        # and offspring (elitism)
        population = self.toolbox.elitism(population + offspring, params.mu_)

    return population