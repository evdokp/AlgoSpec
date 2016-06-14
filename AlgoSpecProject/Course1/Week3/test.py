from Course1.Week3.different_summands import optimal_summands, get_summands
from Course1.Week3.fractional_knapsack import get_optimal_value

for x in range(0, 100):
    print("{0} = {1}".format(x, "+".join([str(y) for y in get_summands(x,1)])))

