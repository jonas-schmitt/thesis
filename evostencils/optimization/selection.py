from deap import tools

def init_multi_objective_selection(self, pset, evaluation_function):
    self.toolbox.register('evaluate', evaluation_function, pset=pset)
    self.toolbox.register("select", tools.selTournamentDCD)
    self.toolbox.register("elitism", tools.selNSGA2)
