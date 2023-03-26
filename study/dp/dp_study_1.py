# brute force

def knapsack_brute_force(values: list[int], weights: list[int], capa: int, curr_index: int) -> int:
    if capa <= 0 or curr_index >= len(values):
        return 0

    selected = 0
    if weights[curr_index] <= capa:  # 현재 선택한 아이템과 용량을 비교
        # 선택하였으니 용량에서 현재 선택한 무게를 뺀 걸 capa로 지정하고 다음 아이템을 index로 넘김
        selected = values[curr_index] + knapsack_brute_force(values, weights, capa - weights[curr_index],
                                                             curr_index + 1)
    # 선택하지 않았으므로 무게는 그대로 두고 다음 아이템으로 재귀 호출
    not_selected = knapsack_brute_force(values, weights, capa, curr_index + 1)

    return max(selected, not_selected)  # 선택과 비선택중 큰 수


# print(knapsack_brute_force([1, 6, 10, 16], [1, 2, 3, 5], 7, 0))
# print(knapsack_brute_force([1, 6, 10, 16], [1, 2, 3, 5], 6, 0))


# dp (top-down)
def knapsack_dp(dp, values: list[int], weights: list[int], capa: int, curr_index: int) -> int:
    indd = weights[curr_index]
    check = dp[curr_index - 1]
    if capa <= 0 or curr_index >= len(values):
        return 0

    if dp[curr_index][capa] != -1:  # 중복된 연산 제거
        return dp[curr_index][capa]

    selected = 0
    if weights[curr_index] <= capa:
        selected = values[curr_index] + knapsack_dp(dp, values, weights, capa - weights[curr_index],
                                                    curr_index + 1)

    not_selected = knapsack_brute_force(values, weights, capa, curr_index + 1)

    dp[curr_index][capa] = max(selected, not_selected)
    return dp[curr_index][capa]


dp1 = [[-1 for _ in range(8)] for _ in range(4)]
print(knapsack_dp(dp1, [1, 6, 10, 16], [1, 2, 3, 5], 7, 0))
dp2 = [[-1 for _ in range(7)] for _ in range(4)]
print(knapsack_dp(dp2, [1, 6, 10, 16], [1, 2, 3, 5], 6, 0))
