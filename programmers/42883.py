# 큰 수 만들기

import itertools


# 다른 풀이
def solution(number, k):
    temp_list = list(itertools.combinations(number, len(number) - k))
    result_list = []
    for temp in temp_list:
        result_list.append(''.join(temp))

    return max(result_list)


# 내 풀이
# def solution(number, k):
#     answer = [number[0]]
#     for num in number[1:]:
#         while answer and k > 0 and num > answer[-1]:
#             answer.pop()
#             k -= 1
#         answer.append(num)
#     return "".join(answer[:-k]) if k > 0 else "".join(answer)


print(solution("1924", 2))

# 19, 24, 92, 14, 94, 12
