import random

def mutate_subtree(individual, min_height, max_height, pset):
    index = random.randrange(len(individual))
    node = individual[index]
    slice_ = individual.searchSubtree(index)

    def condition(height, depth):
        return depth < height
    if random.random() < 0.5:
        subtree = individual[slice_]
    else:
        subtree = None
    new_subtree = generate(pset, min_height, max_height, condition, node.ret, subtree)
    individual[slice_] = new_subtree
    return individual,
