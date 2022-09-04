l = 10 # level
h = 1/2**l # fine-grid spacing
n_h = 1/h - 1
H = 2*h # coarse-grid spacing
n_H = 1/H - 1

# Generate fine and coarse grid
grid = Grid((n_h, n_h), (h, h), l)
coarse_grid = Grid((n_H, n_H), (H, H), l-1)

# Define entities on fine grid
x_h = Approximation("x_h", grid)
b_h = RightHandSide("b_h", grid)
A_h = Operator("A_h", grid)
r_h = Residual(A_h, x_h, b_h)
# Create temporary Cycle node without correction term
x_h = Cycle(x_h, b_h)

# Define entities on coarse-grid
A_H = Operator("A_H", coarse_grid)
x_H = Approximation("x_H", coarse_grid)
b_H = Multiplication(Restriction("I_hH", grid, coarse_grid), r_h)
r_H = Residual(A_H, x_H, b_H)

# Define state on the coarse level
x_H = Cycle(x_H, b_H, r_H, predecessor=x_h)
# Restore iteration on the fine level
x_h = x_H.predecessor
# Replace old correction term with the computed coarse-grid correction
x_h.correction = Multiplication(Prolongation("I_Hh", grid, coarse_grid), x_H)
