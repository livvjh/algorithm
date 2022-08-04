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

