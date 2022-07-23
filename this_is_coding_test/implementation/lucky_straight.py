"""
Quiz. 럭키 스트레이트 기술 사용 (짝수의 n이 입력되고 반을 잘라 좌, 우의 합이 같으면 "Lucky" 출력 다르면 "ready" 출력)
Page. 321
"""
# 입력 짝수로만 숫자로 공백 없이 입력

# 내 코드
n = input()
right_start_index = len(n) // 2
left_end_index = right_start_index - 1  # 3

left_sum = 0  # 좌측 합
right_sum = 0  # 우측 합
for i in range(len(n)):
    if i <= left_end_index:  # 왼쪽 값 합 구하기
        left_sum += int(n[i])
    else:  # 오른쪽 값 합 구하기
        right_sum += int(n[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

# 답 코드

length = len(n)
summary = 0

# 왼쪽 기준의 합 구하기
for i in range(length // 2):  # 6 -> 3 0,1,2
    summary += int(n[i])

# 오른쪽 합 빼기
for i in range(length // 2, length):  # 3,4,5
    summary -= int(n[i])

if summary == 0:  # 값이 오른쪽과 같다는 의미
    print("LUCKY")
else:
    print("READY")
