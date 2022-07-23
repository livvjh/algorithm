n = int(input())

k = input().split()
k.sort()
init_set = [0] * (int(k[n - 1]) + 1)
for i in k:
    init_set[int(i)] = 1

pivot = len(init_set) // 2
result = 0
for i in range(1, len(init_set)):
    if init_set[i] == 1:
        if i > pivot:
            result += i - pivot
        else:
            result += pivot - i

print(pivot)
# 모르겠다