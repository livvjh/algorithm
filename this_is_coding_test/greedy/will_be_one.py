"""
Quiz. 1이 될때까지 - or / 연산을 반복하여 최소한의 연산 횟수 구하기
Page. 99
"""

# 주어진 수 17, 4 1까지 만드는 최소 연산 (n - 1 or n / k)
n, k = map(int, input().split())
count = 0
while n > 1:
    if n % k != 0:
        n -= 1
        count += 1
    else:
        n = n // k
        count += 1
print(count)

# 내 코드
import time

# n, k = map(int, input().split())  # 17, 4
# start_time = time.time()
# count = 0
# while n > 1:
#     if n % k != 0:
#         n -= 1
#         count += 1
#     else:
#         n = n // k
#         count += 1
# print(count)
# end_time = time.time()
# print(f"소요시간 :", format(end_time - start_time, '.5f'), "sec")

# 책 코드

# n, k = map(int, input().split())  # 17, 4
# start_time = time.time()
#
# count = 0
# while True:
#     target = (n // k) * k  # n이 k로 나누어 떨어지는 숫자 target 지정
#     count += n - target  # 주어진 숫자 - target = 반복작업 해야하는 count 횟수
#     n = target
#     if n < k:  # n이 k보다 작을때
#         break
#     n //= k  # n = n//k
#     count += 1
#
# count += n - 1  # 마지막으로 남은 수 -1
# print(count)
# end_time = time.time()
#
# print(f"소요시간 :", format(end_time - start_time, '.5f'), "sec")
