"""
Quiz. 두 배열의 원소 교체
Page. 178
"""
# 배열 A,B가 각 N개씩 원소(자연수)로 구성
# N(각 배열의 길이), K(교체횟수)가 주어지고 최대 K번 원소교체 연산이 있는 배열 A의 원소 최대 합의 값을 구하기
# 입력 (출력 -> 26)
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5


n, k = map(int, input().split())
arr = []
for i in range(2):
    arr.append(list(map(int, input().split())))

a_arr = sorted(arr[0])
b_arr = sorted(arr[1], reverse=True)

for i in range(k):
    if a_arr[i] < b_arr[i]:  # b가 더 클 때만 변경
        a_arr[i] = b_arr[i]
    else:
        break

# result = 0
# for i in a_arr:
#     result += i
# print(result)

print(sum(a_arr))
