"""
   종류: 그리디
   접근방식:
   1. 회의 종료시간 기준 정렬하기 (회의 종료 시간이 빨라야 많이 회의를 진행 가능)
   2. 반복 돌면서 끝시간에 맞춰 바로 이어질 수 있는 시작시간을 비교 (시작시간을 초기화 0으로 해서 end 시간을 temp 0번째 값으로 할당)
   3. 시작시간이 끝시간과 같거나 크면 count + 1, 끝시간을 temp로 설정
   4. 국룰 (정렬, 종료 시간 기준 접근)
"""

# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

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
