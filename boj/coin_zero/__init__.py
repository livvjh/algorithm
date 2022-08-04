n, k = map(int, input().split())

coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

result = 0
for coin in sorted(coin_list, reverse=True):
    if coin > k:
        continue
    result += k // coin
    k %= coin
print(result)
