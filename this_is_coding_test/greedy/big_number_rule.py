"""
Quiz. 큰 수의 법칙 (배열 주어지고 m, k가 주어진다. m은 더하는 횟수, k는 한 숫자당 초과 제한 기준, ex -> [1,3,4] m=5, k=2 --> 4+4+3+4+4 => 19 도출하기)
Page. 92
"""
import time

# 입력
# 5 8 3
# 2 4 5 4 6

# 4 6 3
# 3 4 3 4

# 개선한 내 코드 2
n, m, k = map(int, input().split())
input_arr = list(map(int, input().split()))
arr = []
# 주어진 길이만큼 체크 아니면 0부터 n까지 slice 해서 사용
if len(input_arr) != n:
    arr = input_arr[0:n]
else:
    arr = input_arr

# 정렬
arr.sort(reverse=True)
# 가장 큰 수 * (연속 덧셈 제한 횟수 * (총 연산횟수 // 덧셈 제한 횟수)) => 곱해야할 몫 구하기
count = arr[0] * (k * (m // k))
# 두번째 큰 수 * (나머지 1번씩 두번째 큰수 더하는 횟수)
count += arr[1] * (m % k)
print(count)

# 내 코드
# start_time = time.time()
# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))
#
# arr.sort()  # 가장 큰수, 그다음 큰 수 알기 위한 정렬
#
# max_value = arr[n - 1]
# sec_max_value = arr[n - 2]
# result = 0
#
# count = m // k  # 주어진 입력값에서 3은 8번에서 총 6번 더할 수 있는 것을 의미 이는 3 * 2와 같은 의미이므로 count 몫 구하기
# result += (max_value * k) * count  # 가장 큰 수 * 3회 * 2(몫)
# plus_count = m % k  # 남은 더하는 연산은 몫을 뺀 나머지 갯수만큼
#
# # 5 k 몫은 2 * 2번째 큰수
# result += plus_count * sec_max_value  # 두번째 수와 나머지 갯수를 곱한다
# print(result)
#
# end_time = time.time()
# print(f"소요시간 : {end_time - start_time:.5f} sec")

# 책 코드 good case
# start_time = time.time()
# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))
#
# arr.sort()
#
# fir_value = arr[n - 1]
# sec_value = arr[n - 2]
#
# count = int(m / (k + 1)) * k  # (8/(3+1)) * 3 = 6 , 가장 큰 수가 더해지는 횟수 구하기
# count += m % (k + 1)  # 나머지 0 , 그리고 더하기
#
# result = 0
# result += count * fir_value  # 6 * 6
# result += (m - count) * sec_value  # (8-2) * 5
# print(result)
# end_time = time.time()
# print(f"소요시간 : {end_time - start_time:.5f} sec")

# 책 코드 bad case
# start_time = time.time()
# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))
#
# arr.sort()
# fir_value = arr[n - 1]
# sec_value = arr[n - 2]
#
# result = 0
#
# while True:
#     for i in range(k):  # 가장 큰 수를 k번 더하기 위해 반복
#         if m == 0:  # 더하는 횟수 0 탈출
#             break
#         result += fir_value
#         m -= 1  # result에 큰 수 더할때마다 연산횟수 - 1
#     if m == 0:  # 연산 끝
#         break
#     result += sec_value  # 두번쨰 큰 수 한번 더해주기
#     m -= 1  # 연산 했으니까 -1
# print(result)
#
# end_time = time.time()
# print(f"소요시간 : {end_time - start_time:.5f} sec")
