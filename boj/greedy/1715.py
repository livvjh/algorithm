# 그리디
# 정렬된 두 묶음의 숫자 카드가 있다고 하자.
# 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다.
# 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.


#  예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다.
#  그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법

# n개의 숫자 카드 묶음의 각각 크기 주어질시 최소한의 몇번 비교가 필요한지 구하는 프로그램

# 3, 3, 3, 3, 3
# 6
# 9
# 12
# 15

# 3, 3, 4, 5
# 6
# 9
# 15
# = 30


# n = int(input())
# value_list = []
# for _ in range(n):
#     value_list.append(int(input()))
#
# value_list.sort()
# result_count = 0
# result = 0
# temp_list = []
# for i in range(len(value_list)):
#     result_count += value_list[i]
#     temp_list.append(result_count)
# print(sum(temp_list[1:]))
# 9,3,44,12
# 68


import heapq

n = int(input())
value_list = []
result = 0
for _ in range(n):
    heapq.heappush(value_list, int(input()))
for i in range(n):
    if i == 0:
        continue
    first_val = heapq.heappop(value_list)
    sec_val = heapq.heappop(value_list)
    result += first_val + sec_val
    print(result)
    heapq.heappush(value_list, first_val + sec_val)

# 앞에 2개 더하고 뒤에 2개 더하고 덩어리씩 비교  (홀수면 덩어리 + 낱개)
# 3, 3, 3, 3
# 3, 3 => 6
# 3, 3, 6
# 3, 3 => 6
# 6, 6
# 6+ 6 => 12

# print(result)

# heapq 내장 모듈 사용법
# 이진트리 기반의 최소 힙 자료구조
# minheap을 사용시 정렬된 상태로 추가, 삭제가 되며 가장 작은 원소값은 언제나 0 인덱스에 위치

# heapq 모듈엔 파이썬의 리스트를 마치 힙처럼 다룰 수 있도록 도와줌
# 빈리스트 생성 후 heapq 모듈 호출시마다 생성한 리스트를 인자로 넘기기
