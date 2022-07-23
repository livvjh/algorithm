"""
Quiz. 곱하기 또는 더하기
Page. 312
"""

# 각 숫자 0~9까지 문자열이 주어졌을때 왼쪽부터 오른쪽까지 숫자를 확인하며 + or x 연산을 넣어 가장 큰 최대의 합 구하기

# 내 코드
n = input()

sum = 0
for i in n:
    if sum == 0 or sum == 1:
        sum += int(i)
    else:
        sum *= int(i)

print(sum)

# 책 코드 (두 수에 대해 연산 수행시 하나라도 1 이하(0 or 1)인 경우 더하고, 그외엔 곱하기)
# result = int(n[0])
#
# for i in range(1, len(n)):
#     num = int(n[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
#
# print(result)
