from deap import gp, creator, tools
from evostencils.gp import genGrow, mutInsert

def init_toolbox(pset, min_height, max_height):
    creator.create("Fitness", deap.base.Fitness, weights=(-1.0, -1.0))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.Fitness)

    toolbox = deap.base.Toolbox()
    toolbox.register("tree", genGrow, pset=pset, min_height=min_height, max_height=max_height)
    toolbox.register("mate", gp.cxOnePoint)

    toolbox.register("mutate", mutInsert, pset_=pset, min_height=1, max_height=max_height/2)
    toolbox.register("generate", tools.initIterate, creator.Individual, toolbox.tree)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    return toolbox
