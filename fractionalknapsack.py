def fractional_knapsack(weights, values, capacity):
    ratio = [(v/w, w, v) for v, w in zip(values, weights)]
    ratio.sort(reverse=True)
    
    total = 0
    for r, w, v in ratio:
        if capacity >= w:
            total += v
            capacity -= w
        else:
            total += r * capacity
            break
    return total

# Test
weights = [10, 20, 30]
values = [60, 100, 120]
cap = 50
print("Max Value:", fractional_knapsack(weights, values, cap))  # Output: 240.0
