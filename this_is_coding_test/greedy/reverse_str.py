"""
Quiz. 문자열 뒤집기 (주어진 문자열을 뒤집어서 똑같은 수로 만들기 0001010 => 0000000 근데 이거 1번아님?
Page. 313
"""
import math

input_str = input()

root = int(input_str[0])  # 첫번째 기준 값 구하기
count = 0
for i in range(1, len(input_str)):
    if root == int(input_str[i]):  # 기준 값과 같으면 그대로 진행
        continue
    else:
        root = int(input_str[i])  # 기준값과 다르면 다른 값을 다시 기준값으로 넣기 + 변경 횟수 더하기
        count += 1

count = math.ceil(count / 2)  # 소수점이 있으면 무적권 반올림
print(count)

# 책 코드 (전부 0으로 바꾸는 경우, 전부 1로 바꾸는 경우 더 적은 횟수를 가지는것을 비교하여 계산)
data = input()
count0 = 0  # 전체 0
count1 = 0  # 전체 1

if data[0] == '1':  # 시작 데이터가 1이면
    count0 += 1  # 전체 0으로 변경하는 횟수 +1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

