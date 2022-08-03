n = int(input())

temp_dic = dict()
for key in input().split():
    if temp_dic.get(key) is not None:
        temp_dic[key] += 1
    else:
        temp_dic[key] = 1

given_n = int(input())
result = []
for key in input().split():
    if temp_dic.get(key) is not None:
        result.append(temp_dic[key])
    else:
        result.append(0)

print(*result)
