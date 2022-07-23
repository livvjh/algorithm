# 그리디
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# ex
# 55-50+40 -> -35
# 10-30+20
# 10+20+30+40 -> 100
# 00009-00009 -> 0
import re

# 숫자
# number_list = re.findall("\d+", input_value)

# 특수문자
# special_list = re.findall(r'\+|\-', input_value)


# number_list.sort(reverse=True)

result_list = []
result = 0
for value in input().split('-'):
    count = 0
    for val in value.split('+'):
        count += int(val)
    result_list.append(count)

result = result_list[0]
for i in range(1, len(result_list)):
    result -= result_list[i]
print(result)


# a = input().split('-')
# num = []
# for i in a:
#     cnt = 0
#     s = i.split('+')
#     for j in s:
#         cnt += int(j)
#     num.append(cnt)
# n = num[0]
# for i in range(1, len(num)):
#     n -= num[i]
# print(n)