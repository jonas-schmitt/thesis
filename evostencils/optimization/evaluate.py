from deap import gp

# Implemented as a class method of Optimizer
def evaluate(self, individual, pset, min_level, max_level, evaluation_samples=3, pde_parameter_values=None):
    if pde_parameter_values is None:
        pde_parameter_values = {}

    key = str(individual)
    if key in self.individual_cache:
        return self.individual_cache[key]
    expression, _ = gp.compile(individual, pset)
    solving_time, convergence_factor, number_of_iterations = self.program_generator.generate_and_evaluate(expression, min_level, max_level, evaluation_samples, pde_parameter_values)

    fitness = convergence_factor, solving_time / number_of_iterations
    self.individual_cache[key] = fitness
    return fitness
