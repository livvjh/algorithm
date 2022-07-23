"""
Quiz. 숫자 카드게임 (주어진 카드중 행마다 가장 작은 수를 찾고 그 목록중 가장 큰 수를 찾기)
Page. 96
"""

n, m = map(int, input().split())

arr_set = []
for _ in range(n):
    arr_set.append(list(map(int, input().split())))

result = min(arr_set[0])
for arr in arr_set:
    if result < min(arr):
        result = min(arr)

print(result)


# 내 코드
# n, m = map(int, input().split())  # n => row 갯수
#
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#
# result = min(arr[0])
# for i in range(len(arr)):
#     if result < min(arr[i]):
#         result = min(arr[i])
#
# print(result)

# 책 코드
# n, m = map(int, input().split())
#
# result = 0
# for _ in range(n):
#     data = list(map(int, input().split()))
#     min_val = min(data)
#     result = max(min_val, result)
#
# print(result)
