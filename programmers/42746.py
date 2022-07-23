# 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return ''.join(numbers)


# timeout
# def solution(numbers):
#     from itertools import permutations
#     permutation_list = permutations(numbers)
#     temp_list = []
#     for permutation in permutation_list:
#         demo = [str(p) for p in permutation]
#         temp_list.append("".join(demo))
#     temp = sorted(temp_list, reverse=True)
#     return temp[0]


print(solution([3, 30, 34, 5, 9]))
