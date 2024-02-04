def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight, value = items[i - 1]
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruction of the items included
    included_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            weight, value = items[i - 1]
            included_items.append((weight, value))
            w -= weight

    return dp[n][capacity], included_items

# Main program
items = [(16, 72), (4, 12), (8, 24), (6, 32), (12, 18), (10, 20)]
capacity = 30
max_profit, selected_items = knapsack(items, capacity)

print("Maximum Profit:", max_profit)
print("Selected Items (weight, value):", selected_items)
