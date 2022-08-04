n = int(input())
value_set = list(map(int, input().split()))
value_set.sort()
print(value_set[0], value_set[len(value_set) - 1], end=" ")
