number_of_smoothers = 2
minimum_smoothing_steps = 4
maximum_smoothing_steps = 15
s = 0.0
for i in range(minimum_smoothing_steps, maximum_smoothing_steps + 1):
    s += (number_of_smoothers * 3)**i

print(s)
