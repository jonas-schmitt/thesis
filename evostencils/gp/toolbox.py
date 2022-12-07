from deap import base, gp, creator
from evostencils.gp import genGrow, mutInsert

def init_toolbox(self, pset, min_height, max_height, multi_objective=True):
    # Define an Individual together with its Fitness
    if multi_objective:
        creator.create("Fitness", base.Fitness, weights=(-1.0, -1.0))
    else:
        creator.create("Fitness", base.Fitness, weights=(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.Fitness)

    self.toolbox = deap.base.Toolbox()

    # Population Initialization
    self.toolbox.register("generate_tree", genGrow, pset=pset, min_height=min_height, max_height=max_height)
    self.toolbox.register("generate_individual", tools.initIterate, creator.Individual, self.toolbox.generate_tree)
    self.toolbox.register("population", tools.initRepeat, list, self.toolbox.generate_individual)
    
    # Crossover and Mutation
    self.toolbox.register("mate", gp.cxOnePoint)
    self.toolbox.register("mutate", mutateSubtree, pset_=pset, min_height=1, max_height=max_height / 2)
