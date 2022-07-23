"""
Quiz. 모험가 길드
Page. 311
"""
# 36분까지
# 입력 (출력 -> 27 15 12)
# 3
# 15
# 27
# 12


n = int(input())

arr = list(map(int, input().split()))
arr.sort()

# 숫자만큼의 그룹으로 묶기
# 3
# 1 2 2
# check = [0] * n
# check[0] = arr[0]
# 1 2 2
# 2 1 2
# 1 2 2

# 2 3 3


count = 0  # 모험가
result = 0
for i in arr:  # i는 공포도
    count += 1  # 모험가 추가
    if count >= i:  # 모험가의 수가 현재 공포도보다 클때 그룹 결성
        result += 1  # 결과 값 +1
        count = 0  # 모험가 초기화

print(result)
