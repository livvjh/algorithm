# 실패 코드
# n = int(input())
# value_list = []
# for _ in range(n):
#     value_list.append(int(input()))
#
# value_list.sort()
# result_count = 0
# result = 0
# temp_list = []
# for i in range(len(value_list)):
#     result_count += value_list[i]
#     temp_list.append(result_count)
# print(sum(temp_list[1:]))


import heapq

n = int(input())
value_list = []
result = 0
for _ in range(n):
    heapq.heappush(value_list, int(input()))
for i in range(n):
    if i == 0:
        continue
    first_val = heapq.heappop(value_list)
    sec_val = heapq.heappop(value_list)
    result += first_val + sec_val
    heapq.heappush(value_list, first_val + sec_val)

print(result)

# n = int(input())
# card = []
# for c in range(n):
#     heapq.heappush(card, int(input()))
#
# sol = 0
#
# if len(card) == 1:
#     print(sol)
#
# else:
#     while (len(card) > 1):
#         min1 = heapq.heappop(card)
#         min2 = heapq.heappop(card)
#         sol += min1 + min2
#         heapq.heappush(card, min1 + min2)
#
#     print(sol)
