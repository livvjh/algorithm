"""
    종류: 등차수열
    등차수열이란?
    123인 경우 1 - 2 - 3 공차가 1인 등차수열
    연속적인 수의 갯수가 3개 이상일 경우부터 해당 등차수열이 성립됌
    즉 1~99까지는 무조건 등차수열
    101 등차수열 x (1 -> 0 이 -1인데 세번째 1이 나옴)
"""

input_val = int(input())
result = 0

for i in range(1, input_val + 1):
    tmp = str(i)[0]
    if i < 100:
        result += 1
    else:
        temp_list = list(map(int, str(i)))
        if temp_list[0] - temp_list[1] == temp_list[1] - temp_list[2]:
            result += 1

print(result)
