# 구현
# 선영이의 집에는 콘센트를 꽂을 수 있는 플러그가 하나밖에 없다. 선영이는 많은 컴퓨터를 가지고 있는데, 컴퓨터의 전원 문제는 어떻게 해결하는 것일까?
# 하나의 플러그가 있고, N개의 멀티탭이 있다. 각 멀티탭은 몇 개의 플러그로 이루어져 있다고 한다. 최대 몇 대의 컴퓨터를 전원에 연결할 수 있을까?

# 첫째 줄에 최대로 전원에 연결될 수 있는 컴퓨터의 수를 출력한다.
import sys

# python3 전용
n = int(sys.stdin.readline())
result = 0
for i in range(n):
    result += int(sys.stdin.readline())

print(result - (n - 1))


