"""
   종류: 그리디
   접근방식: 주어진 동전갯수(화폐)리스트를 반복으로 돌면서 주어진 K원을 나눈 몫을 count 갯수로 추가하고
    나머지값을 지속적으로 변수에 할당하여 나누어 갯수 구하기
   소요시간: O(n)
"""

# 동전
# 동전을 리스트로 받는다
# 반복 돌면서 해당 화폐보다 제시한 금액이
# 작을때만 ㄱㄱ
# 몫을 count로 수집
# 나머지 값을 다시 제시한 금액으로 변수 넣기


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
