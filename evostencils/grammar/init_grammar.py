import numpy as np
from evostencils.ir import partitioning
from evostencils.grammar.gp import PrimitiveSetTyped

def init_grammar(generator, x_h, b_h, max_level, samples, coarsest=False):
    A_h = generator.get_operator(max_level)
    restriction_operators, prolongation_operators = generator.get_inter_grid_operators(max_level, max_level - 1)
    A_2h = generator.get_operator(max_level - 1)
    partitionings = [partitioning.RedBlack]
    CGS_2h = CoarseGridSolver("CGS", A_2h)
    relaxation_factor_interval = np.linspace(0.1, 1.9, samples)
    terminals = Terminals(x_h, A_h, A_2h, restriction_operators, prolongation_operators, CGS_2h, relaxation_factor_interval, partitionings)
    types = Types(0)
    pset = PrimitiveSetTyped("main", [], types.S_h)
    pset.addTerminal((x_h, b_h), types.S_guard_h, 'initial_state')
    pset.addTerminal(terminals.no_partitioning, types.Partitioning, terminals.no_partitioning.get_name())
    for p in terminals.partitionings:
        pset.addTerminal(p, types.Partitioning, p.get_name())
    for i in range(0, samples):
        pset.addTerminal(i, types.RelaxationFactorIndex)

    add_level(pset, terminals, types, max_level, 0, samples, coarsest=coarsest)
    return pset, terminals, types
