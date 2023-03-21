# brute force

def knapsack_brute_force(values: list[int], weights: list[int], capa: int, curr_index: int) -> int:
    if capa <= 0 or curr_index >= len(values):
        return 0

    selected = 0
    if weights[curr_index] <= capa:
        selected = values[curr_index] + knapsack_brute_force(values, weights, capa - weights[curr_index],
                                                             curr_index + 1)
    not_selected = knapsack_brute_force(values, weights, capa, curr_index + 1)

    return max(selected, not_selected)


print(knapsack_brute_force([1, 6, 10, 16], [1, 2, 3, 5], 7, 0))
print(knapsack_brute_force([1, 6, 10, 16], [1, 2, 3, 5], 6, 0))
