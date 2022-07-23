"""
Quiz. 미로탈출 (bfs)
Page. 152
"""
# n * m 크기 직사각형에 위치 (1,1)을 시작점으로 출구 (n,m)까지 움직여야 하는 최소칸의 갯수
# 움직일 수 있는 칸은 1, 괴물 있는 부분은 0 (0은 못감)

# 입력
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 주어진 첫번째 인덱스를 queue에 넣기

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 4방향 (상하좌우)
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위 벗어났을때 무시
                continue

            if graph[nx][ny] == 0:  # 벽일때 무시
                continue

            if graph[nx][ny] == 1:  # 이동 가능한 노드
                graph[nx][ny] = graph[x][y] + 1  # 해당 값에 이전 경로값 + 1씩 하기
                queue.append((nx, ny))  # 현재 노드를 다시 queue에 추가

    return graph[n - 1][m - 1]  # 가장 마지막 인덱스의 값을 반환


print(bfs(0, 0))
# 101010
# 111111
# 000001
# 111111
# 111111
