"""
Quiz. 상하좌우 (여행가의 이동 경로를 입력하면 최종 목적지 좌표 출력하기)
Page. 110
"""
import time

# start_point = 1,1 (0,0 x)
# up [x-1, y]
# down [x+1, y]
# left [x, y-1]
# right [x, y+1]

# 1,1에선 up과 left가 허용되지 않음 (무시)

# 내 코드
# start_time = time.time()
# n = int(input())
# move_sign = input().split()
# x, y = 1, 1
#
# for k in range(len(move_sign)):
#     if move_sign[k] == 'R':
#         if y + 1 > n:
#             continue
#         else:
#             y += 1
#     elif move_sign[k] == 'L':
#         if y - 1 < 2:
#             continue  # if만 빠져나가
#         else:
#             y -= 1
#     elif move_sign[k] == 'U':
#         if x - 1 < 2:
#             continue
#         else:
#             y -= 1
#     elif move_sign[k] == 'D':
#         if x + 1 > n:
#             continue
#         else:
#             x += 1
#
# print(x, y)
# end_time = time.time()
# print(f"소요시간 : {end_time - start_time:.5f} sec")


# 다시 풀기
n = int(input())
move_list = input().split()

x, y = 1, 1
for move in move_list:
    if move == 'r':
        if y + 1 > n:
            continue
        y += 1
    elif move == 'u':
        if x - 1 == 0:
            continue
        x -= 1
    elif move == 'd':
        if x + 1 > n:
            continue
        x += 1
    elif move == 'l':
        if y - 1 == 0:
            continue
        y -= 1
print(x, y)

# 책 코드
# start_time = time.time()
# n = int(input())
# plans = input().split()
# x, y = 1, 1
#
# # L, R, U, D의 이동 방향 배열
# # L은 [dx[0], dy[0]] -> 0, -1
# # R은 [dx[1], dy[1]] -> 0, 1
# # U은 [dx[2], dy[2]] -> -1, 0
# # D은 [dx[3], dy[3]] -> 1, 0
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# move_types = ['L', 'R', 'U', 'D']
#
# for plan in plans:  # 이동할 좌표 목록
#     for i in range(len(move_types)):  # move_type들과 비교해서 맞는지 찾기 (R==R)
#         if move_types[i] == plan:
#             nx = x + dx[i]  # 시작 좌표 x + type x 이동값
#             ny = y + dy[i]  # 시작 좌표 y + type y 이동값
#
#     if nx < 1 or ny < 1 or nx > n or ny > n:  # 범위 초과 무시
#         continue
#     x, y = nx, ny
# print(x, y)
#
# end_time = time.time()
# print(f"소요시간 : {end_time - start_time:.5f} sec")


