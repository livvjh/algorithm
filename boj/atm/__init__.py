n = int(input())
times = list(map(int, input().split()))

times.sort()
temp_sum = 0
accumulate_time = 0
for time in times:
    temp_sum += time
    accumulate_time += temp_sum
print(accumulate_time)
