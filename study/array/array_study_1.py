# brute force
def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]


print(two_sum_brute_force([2, 7, 8, 11], 9))


# hash table
def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
    temp_dict = {}
    for i, v in enumerate(nums):
        value = target - v
        if temp_dict.get(value) is not None and temp_dict[value] != i:  # and 조건은 값의 중복 허용 x
            return sorted([i, temp_dict[value]])
        temp_dict[v] = i
    return [-1, -1]


print(two_sum_hash_table([2, 7, 8, 11], 9))
