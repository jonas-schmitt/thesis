import random

def evaluate_individuals(self, invalid_ind):
    fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

def create_offspring(self, parents, crossover_probability):
    offspring = []
    for ind1, ind2 in zip(parents[::2], parents[1::2]):
        child1, child2 = ind1, ind2
        key1, key2 = None, None
        count = 0
        operator_choice = random.random()
        while key1 or key2 in self.individual_cache and count < 10:
            if operator_choice < crossover_probability:
                child1, child2 = self.toolbox.mate(ind1, ind2)
            else:
                child1, = self.toolbox.mutate(ind1)
                child2, = self.toolbox.mutate(ind2)
            key1, key2 = str(child1), str(child2)
            count += 1
        del child1.fitness.values, child2.fitness.values
        offspring.extend([child1, child2])
    return offspring
