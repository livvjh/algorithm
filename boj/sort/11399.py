"""
   종류: 정렬
   접근방식: 걸린 시간이 누적해서 더해지기 떄문에 돈 인출 시간을 기준으로 오름차순 정렬 후
   해당 값의 합을 리턴한다.
   소요시간: O(n)
"""


def solution(n, times):
    times.sort()
    temp_sum = 0
    accumulate_time = 0
    for time in times:
        temp_sum += time
        accumulate_time += temp_sum
    return accumulate_time


print(solution(5, [3, 1, 4, 3, 2]))
