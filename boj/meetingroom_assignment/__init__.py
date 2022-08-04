n = int(input())
conference_list = []
for _ in range(n):
    start_time, end_time = map(int, input().split())
    conference_list.append((start_time, end_time))

conference_list.sort(key=lambda x: (x[1], x[0]))

temp_end_time = 0
count = 0
for conference in conference_list:
    start_time = conference[0]
    end_time = conference[1]

    if temp_end_time <= start_time:
        temp_end_time = end_time
        count += 1
print(count)
