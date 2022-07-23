"""
Quiz. 거스름돈 최소로 거슬러주기
Page. 87
"""

# 내 코드
n = 1260
count = 0
coin_array = [500, 100, 50, 10]

for coin in coin_array:
    count += n // coin  # 거스름돈으로 각 동전별 거슬러줄 수 있는 개수 세기
    n = n % coin  # 해당 금액을 현재 동전으로 거스르고 남은 돈
print(count)
