from deap import tools

def init_multi_objective_selection(toolbox, evaluation_function, pset):
    toolbox.register('evaluate', evaluation_function, pset=pset)
    toolbox.register("select", tools.selTournamentDCD)
    toolbox.register("elitism", tools.selNSGA2)
    return toolbox
