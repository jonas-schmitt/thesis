number_of_smoothers = 2
minimum_smoothing_steps = 4
maximum_smoothing_steps = 30
s = 0.0
for i in range(minimum_smoothing_steps, maximum_smoothing_steps + 1):
    s += (number_of_smoothers * 3)**i

print(s)

nu_1 = 2
nu_2 = 1
gamma = 2
level = 4
s = 0.0
for i in range(0, level):
    # s += gamma**i * (nu_1 + nu_2)
    s += 0.5 * (gamma**i * (nu_1 + nu_2) + (nu_1 + nu_2))
print(s)