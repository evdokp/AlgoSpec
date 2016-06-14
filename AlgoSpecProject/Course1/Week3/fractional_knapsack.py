# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    total_weights = sum(weights)
    vpus = [[w,v/w] for (w,v) in zip(weights, values)]
    vpus_sorted = sorted(vpus, reverse=True, key=lambda compound: compound[1])
    filled = 0
    rem_capacity = capacity
    value = 0.0
    compound_idx = 0
    is_finished = False
    while not is_finished:
        mass_to_add = min(rem_capacity, vpus_sorted[compound_idx][0])
        value += mass_to_add * vpus_sorted[compound_idx][1]
        vpus_sorted[compound_idx][0] -= mass_to_add
        rem_capacity -= mass_to_add
        filled += mass_to_add
        if vpus_sorted[compound_idx][0] == 0:
            compound_idx += 1
        is_finished = rem_capacity == 0
        if not is_finished:
            is_finished = filled == total_weights

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
