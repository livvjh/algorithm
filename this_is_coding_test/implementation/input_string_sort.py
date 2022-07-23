"""
Quiz. 문자열 재정렬 (알파벳, 숫자가 합쳐진 문자열이 입력되고 입력된 문자열에서 알파벳은 오름차순, 숫자는 숫자의 합을 더해 붙여서 출력한다.
Page. 322
"""
# 입력 (출력 -> ABCKK13, ADDIJJJKKLSS20)
# K1KA5CB7
# AJKDLSI412K4JSJ9D

# 내 코드
import re

input_data = input()
numbers = re.findall("\d", input_data)
strings = re.findall("\D", input_data)
strings.sort()
num = 0
for number in numbers:
    num += int(number)
result_num = str(num)
result_str = "".join(strings)
print(result_str + result_num)

result = []
val = 0

for x in input_data:
    if x.isalpha():
        result.append(x)
    else:
        val += int(x)
result.sort()
if val != 0:  # 숫자가 존재한다면
    result.append(str(val))  # string으로 변환해서 추가
print("".join(result))
