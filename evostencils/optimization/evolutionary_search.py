import random

def evolutionary_search(self, initial_population_size, generations, mu_, lambda_, crossover_probability, mutation_probability, use_random_search=False):
    # Generate initial population
    population = self.toolbox.population(n=initial_population_size)

    invalid_ind = [ind for ind in population]
    fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit
    # Select mu individuals from the initial population
    population = self.toolbox.select(population, mu_)
    for gen in range(1, generations + 1):
        if use_random_search:
            # For random search simply generate individuals randomly
            offspring = self.toolbox.population(n=lambda_)
        else:
            # Select lambda parents for mutation and crossover
            selected = self.toolbox.select_for_mating(population, lambda_)
            parents = [self.toolbox.clone(ind) for ind in selected]
            offspring = []
            for ind1, ind2 in zip(parents[::2], parents[1::2]):
                operator_choice = random.random()
                if operator_choice < crossover_probability:
                    child1, child2 = self.toolbox.mate(ind1, ind2)
                elif operator_choice < crossover_probability + mutation_probability + self.epsilon:
                    child1, = self.toolbox.mutate(ind1)
                    child2, = self.toolbox.mutate(ind2)
                else:
                    child1 = ind1
                    child2 = ind2
                del child1.fitness.values, child2.fitness.values
                offspring.extend([child1, child2])
        # Evaluate new individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        # Select new population from the combined set of parents
        # and offspring (elitism)
        population = self.toolbox.select(population + offspring, mu_)

    return population