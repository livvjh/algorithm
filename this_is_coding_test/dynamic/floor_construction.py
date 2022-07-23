"""
Quiz. 바닥공사 가로 길이 n 세로 길이 2인 직사각형 형태의 바닥이 있을때 1x2, 2x1, 2x2 덮개를 이용해 바닥을 채우기 위해 채울 수 있는 경우의 수 구하기
Page. 223
"""

# 입력 (출력 -> 5)
# 3
# 40분까지

d = [0] * 1001
# n = int(input())

d[1] = 1  # 2*1 은 1개밖에 방법이 없음
d[2] = 3  # 2*2는 2*2 1개, 2*1 || 1개, 1*2 = 1개 총 3개

# for i in (3, n + 1):  # 이후 3부터 갯수를 세어야 함
#     d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# print(d[n])

