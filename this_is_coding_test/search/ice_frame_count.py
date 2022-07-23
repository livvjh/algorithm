# 얼음 틀에 생성되는 아이스크림 갯수 구하기
# dfs

"""
Quiz. 음료 얼려 먹기 (dfs)
Page. 149
"""
# n * m 크기 얼음 틀 구멍이 있는 부분 0, 칸막이 1일때 구멍이 상,하,좌,우로 연결되어 있으면 이를 1개로 본다
# 생성되는 총 아이스크림의 갯수는? 0으로 붙어 있는 칸의 갯수 구하기

# 입력 (3개)
# 00110
# 00011
# 11111
# 00000

n, m = map(int, input().split())

# coordinate = [[0] * (n + 1) for i in range(n + 1)] 1,1 로 시작하는 2차 배열 생성
# ice_frame = [[0] * m for _ in range(n)]  # n = row, m = column
# for i in range(n):
#     ice_frame[i] = list(map(int, input()))

# 한번에 처리
ice_frame = []
for i in range(n):
    ice_frame.append(list(map(int, input())))


# 상, 하, 좌, 우
# [-1, 0], [1, 0], [0, -1], [0, 1]

# 좌표 방문 여부 체크 (return True일때마다 결과값을 +1 하기)
def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:  # 범위 벗어나는지 체크 (벗어나면 False)
        return False

    if ice_frame[x][y] == 0:
        ice_frame[x][y] = 1  # 방문처리
        # 재귀
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print("아이스 갯수: ", result)

