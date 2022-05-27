from deap import gp

def evaluate(self, individual, pset, min_level, max_level, evaluation_samples=3, pde_parameter_values=None):
    if pde_parameter_values is None:
        pde_parameter_values = {}
    if self.individual_in_cache(individual):
        return self.get_cached_fitness(individual)
    expression, _ = gp.compile(individual, pset)
    solving_time, convergence_factor, number_of_iterations = self.program_generator.generate_and_evaluate(expression, min_level, max_level, evaluation_samples, pde_parameter_values)
    fitness = convergence_factor, solving_time / number_of_iterations
    self.add_individual_to_cache(individual, fitness)
    return fitness
