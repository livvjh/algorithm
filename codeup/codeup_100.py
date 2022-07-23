# 6017
# str = input()
# new_str = str
# for i in range(3):
#     if i != 2:
#         new_str += " " + str
#
# print(new_str)


# 6081
# n = int(input(), 16)
# for i in range(1, 16):
#     print('%X' % n, '*', '%X' % i, '=%X' % (n * i), sep='')

# 6082
# n = int(input())
# result = ""
# for i in range(1, n + 1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         result += "X"
#     else:
#         result += str(i)
#     if i != n:
#         result += " "
# print(result)

# 6083
# a, b, c = map(int, input().split())
# count = 0
# for i in range(a):
#     for j in range(b):
#         for k in range(c):
#             print(i, j, k)
#             count += 1
# print(count)

# 6084
# 녹음시간 s, 스테레오 c, bit b, hz h
# h, b, c, s = map(int, input().split())
# result = (h * b * c * s) / 8 / 1024 / 1024
# print(format(result, '.1f'), 'MB')


# 6086
# a = int(input())
# sum = 0
# for i in range(1, a + 1):
#     sum += i  #
#     if sum >= a:
#         print(sum)
#         break


# 6087
# n = int(input())
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         continue
#     print(i, end=' ')

# 6088 (등차 같은 수열 -> 차이가 같은 수의 나열)
# a 시작값, b 등차값, c 몇번째 수를 알고 싶은지
# ex -> 1 3 5 입력시 -> 1 4 7 10 (13) 이 나와야함 13만 출력

# a, b, c = map(int, input().split())
# data_list = []
# i = 0
# while i < c:
#     data_list.append(a)
#     a += b
#     i += 1
# print(data_list[c - 1])

# a, b, c = map(int, input().split())
# total = a
# for _ in range(c-1):
#     total = total + b
# print(total)

# 6089 (등차 같은 수열 -> 차이가 같은 수의 나열)
# a, r, n = map(int, input().split())
# total = a
# for _ in range(n-1):
#     total *= r
# print(total)

# 6090 (시작:a, 곱할값:m, 더할값:d, 몇번째수:n)
# a, m, d, n = map(int, input().split())
# result = a
# for _ in range(n - 1):
#     result = (result * m) + d
#
# print(result)


# 6091 (겹치는 날짜 구하기)

# 3 6 9 12 15 18 21
# 14 21 28 35 42 49 56 63
# 27 36 45
# a, b, c = map(int, input().split())
# day = 1
# # day에 각 출석일이 나누어 떨어지지 않으면 계속 day추가하기
# while day % a != 0 or day % b != 0 or day % c != 0:
#     day += 1
# print(day)

# 6092 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.
# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

# n = int(input())  # 불린 횟수
# a = input().split()  # 픽한 번호들
#
# for i in range(n):
#     a[i] = int(a[i])
#
# tmp_list = [0] * 23
#
# for i in range(n):
#     tmp_list[a[i]-1] += 1
#
# for data in tmp_list:
#     print(data, end=' ')


# 6093
# n = int(input())
# a = input().split()
#
# a.reverse()
# print(" ".join(a))

# 6094

# n = int(input())
# a = [int(x) for x in input().split()]  # 10이 있으면 2보다 작다 처리함 (그래서 int로 변환)
# a.sort()
# print(a[0])


# 6095 오목판 돌 위치 구하기
# 1. 일단 바둑판 다 0으로 초기화
# 2. 선택된 애들을 입력받기 [[n, m], [n, m], [n, m], [n, m], [n, m]]

n = int(input())
arr = [[0] * 19 for _ in range(19)]

for _ in range(n):
    checked_arr = input().split()
    arr[int(checked_arr[0])-1][int(checked_arr[1])-1] = 1

for i in range(len(arr)):
    for j in arr[i]:
        print(j, end=" ")
    print()


# 6096
# arr = [[0] * 19 for _ in range(19)]  # 19, 19 바둑판 0으로 초기화
#
# for i in range(19):
#     arr[i] = list(map(int, input().split()))  # 입력값으로 변경처리
#
# n = int(input())
#
# for i in range(n):
#     x, y = map(int, input().split())
#
#     for j in range(19):
#         if arr[x - 1][j] == 0:
#             arr[x - 1][j] = 1
#         else:
#             arr[x - 1][j] = 0
#
#         if arr[j][y - 1] == 0:
#             arr[j][y - 1] = 1
#         else:
#             arr[j][y - 1] = 0
#
# for i in range(19):
#     for j in range(19):
#         print(arr[i][j], end=" ")
#     print()


# 6097
# width, height = map(int, input().split())  # 20, 10 => 1차원 배열 length가 10
# n = int(input())
# arr = [[0] * height for _ in range(width)]
# # arr = 20, 10
#
#
# while n > 0:
#     length, d, x, y = map(int, input().split())  # x,y 는 시작점 좌표인데 1부터 시작
#     if d == 0:
#         for _ in range(length):
#             arr[x - 1][y - 1] = 1
#             y = y + 1
#     else:
#         for _ in range(length):
#             arr[x - 1][y - 1] = 1
#             x = x + 1
#     n -= 1
#
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         print(arr[i][j], end=" ")
#     print()

# 여기서 시작점을 가지고 총 length 와 d를 활용해 가로,세로 구분을 통해 최종 목적지 x,y를 구해야함
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if d == 0:  # 가로 (x+1)
#             # 1. length만큼 반복해야함
#             # 2. 반복할때 x+1
#             if length:
#                 arr[i + 1][j]
#
#         else:  # 세로 (y+1)
#             pass


# 6097 모범답안

# coordinate = [[0] * (n + 1) for i in range(n + 1)]  # 1,1부터 시작하는 2차 배열 초기화  [0,1,2,3,4,5] 면 0은 안씀
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         pass
#     print()

# h,w = input().split()
# h = int(h)
# w = int(w)
#
# m = []
# for i in range(h+1) : # 0은 무시하고 쓰기 1~h+1까지
#   m.append([]) //첫번째 빈 배열
#   for j in range(w+1) :
#     m[i].append(0)
#
# n = int(input())
# for i in range(n) :
#   l,d,x,y = input().split()
#   if int(d)==0 :
#     for j in range(int(l)) :
#       m[int(x)][int(y)+j] = 1
#   else :
#     for j in range(int(l)) :
#       m[int(x)+j][int(y)] = 1
#
# for i in range(1, h+1) :
#   for j in range(1, w+1) :
#     print(m[i][j], end=' ')
#   print()


# 6098
# arr = [[0] * 10 for _ in range(10)]  # 초기화 후
# arr.insert(0, [])
# for i in range(1, 11):
#     arr[i] = list(map(int, input().split()))  # 입력된 값으로 변경
#     arr[i].insert(0, [])
# # print("------------------------------")
#
# x, y = 2, 2
# while True:
#     if arr[x][y] == 0:  # 0일때 좌표 찍기
#         arr[x][y] = 9
#     elif arr[x][y] == 2:  # 끝 부분 변경 후 종료
#         arr[x][y] = 9
#         break
#
#     if arr[x][y + 1] == 1 and arr[x + 1][y] == 1: #막다른길 오른쪽/아래 둘다 막힐때 역시 종료
#         break
#     else:
#         if arr[x][y + 1] != 1:  # 오른쪽에 1이 아니면 갈수 있으므로 y축 + 1해서 -> 오른쪽 이동
#             y += 1
#         elif arr[x + 1][y] != 1: # 위에 조건에서 1 즉 벽으로 막혀있을때 조건 아래로 이동하는데 이동하는 칸의 값이 1이 아닐땐 x를 더해 한칸 더 내려간다
#             x += 1
#
# print("--------------------------------")
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(arr[i][j], end=" ")
#     print()
