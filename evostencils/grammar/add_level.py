def add_level(pset: PrimitiveSetTyped, terminals: Terminals, types: Types, max_level, depth, coarsest=False):
    add_terminals(pset, terminals, types, max_level, depth, coarsest)
    level = max_level - depth

    def add_primitive(pset, f, fixed_types, input_types, output_types, name):
        for t1, t2 in zip(input_types, output_types):
            pset.addPrimitive(f, fixed_types + [t1], t2, name)

    # Productions
    add_primitive(pset, residual, [], [types.S_h, types.S_guard_h], [types.C_h, types.C_guard_h], f"residual_{level}")

    add_primitive(pset, jacobi, [types.RelaxationFactorIndex, types.Partitioning], [types.C_h, types.C_guard_h], [types.S_h, types.S_guard_h], f"jacobi_{level}")
    # Include additional smoothers here

    if not coarsest:
        add_primitive(pset, update_with_coarse_grid_correction, [types.RelaxationFactorIndex, types.P_2h], [types.S_2h, types.S_guard_2h], [types.S_h, types.S_guard_h], f"update_with_coarse_grid_correction_{level}")

        add_primitive(pset, coarsening, [types.A_2h, types.x_2h, types.R_h], [types.C_h, types.C_guard_h], [types.C_2h, types.C_guard_2h], f"coarsening_{level}")
    else:
        # Add transition C_guard_h <- S_h to enable derivation termination
        add_primitive(pset, correct_with_coarse_grid_solver, [types.RelaxationFactorIndex, types.P_2h, types.CGS_2h, types.R_h], [types.C_h, types.C_guard_h], [types.S_h, types.S_h], f'correct_with_coarse_grid_solver_{level}')
        pset.addTerminal(terminals.coarse_grid_solver, types.CGS_2h, f'CGS_{level - 1}')
