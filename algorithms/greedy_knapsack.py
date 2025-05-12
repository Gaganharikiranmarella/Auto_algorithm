def greedy_knapsack(weights, values, capacity):
    ratio = [(v/w, w, v) for v, w in zip(values, weights)]
    ratio.sort(reverse=True)
    total_value = 0
    for r, w, v in ratio:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            total_value += r * capacity
            break
    return total_value
