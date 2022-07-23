"""
Quiz. 왕실의 나이트 8*8 체스판에서 나이트의 위치가 주어졌을때 움직일 수 있는 경우의 수 출력
Page. 115
"""
import time

start_time = time.time()
# 내 코드
# 움직일 수 있는 경로 총 8개
# [-1, 2]
# [-2, 1]
# [-2, -1]
# [-1, -2]
# [1, -2]
# [2, -1]
# [2, 1]
# [1, 2]
# 데이터 변경 불가능하고 list보다 속도 더 빠른 tuple 사용
steps = [
    (-1, 2),
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1),
    (2, 1),
    (1, 2)
]
# row 는 a, b, c
# fields 는 1,2,3
value = input()
row = ord(value[0])  # 97, [x][y] 에서 y에 해당
column = int(value[-1])  # [x][y]에서 x에 해당

count = 0
for step in steps:
    # 105는 a(97)에서 8의 범위를 더한 값, 해당 범위를 벗어나면 continue(밖으로 빠져나가 for문으로)
    if column + step[0] < 1 or column + step[0] > 8 or row + step[1] < 97 or row + step[1] > 105:
        continue
    count += 1
print(count)

end_time = time.time()
print(f"소요시간 : {end_time - start_time:.5f} sec")

# 책 코드
# value = input()
# row = int(value[1])  # x에 해당
# column = int(ord(value[0])) - int(ord('a')) + 1  # y에 해당 (97 - 97) +1 (1부터 시작)
#
# steps = [
#     (-1, 2),
#     (-2, 1),
#     (-2, -1),
#     (-1, -2),
#     (1, -2),
#     (2, -1),
#     (2, 1),
#     (1, 2)
# ]
# result = 0
#
# for step in steps:
#     next_row = row + step[0]
#     next_col = column + step[1]
#
#     if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:  # 범위 안에 들었을때 count + 1
#         result += 1
# print(result)
