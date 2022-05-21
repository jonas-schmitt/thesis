from deap import base, gp, creator
from evostencils.gp import genGrow, mutInsert

def init_toolbox(pset, min_height, max_height, multiobjective=True):
    # Define an Individual together with its Fitness
    if multiobjective:
        creator.create("Fitness", base.Fitness, weights=(-1.0, -1.0))
    else:
        creator.create("Fitness", base.Fitness, weights=(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.Fitness)

    toolbox = deap.base.Toolbox()

    # Population Initialization
    toolbox.register("generate_tree", genGrow, pset=pset, min_height=min_height, max_height=max_height)
    toolbox.register("generate_individual", tools.initIterate, creator.Individual, toolbox.generate_tree)
    toolbox.register("population", tools.initRepeat, list, toolbox.generate_individual)

    # Crossover and Mutation
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("mutate", mutInsert, pset_=pset, min_height=1, max_height=max_height/2)


    return toolbox
