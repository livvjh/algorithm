"""
Quiz. 위에서 아래로 (n개의 길이만큼 숫자가 주어진다. 해당 숫자들을 내림차순으로 정렬)
Page. 178
"""
# 입력 (출력 -> 27 15 12)
# 3
# 15
# 27
# 12

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
for num in arr:
    print(num, end=" ")
