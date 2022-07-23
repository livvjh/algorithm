"""
Quiz. 부품 찾기 (이진탐색)
Page. 113
"""
# 전자 제품 재고 수량 n과 n개의 부품 데이터 입력 (공백 기준)
# 찾고자 하는 부품이 있는지 확인 n개의 갯수와 n개의 찾는 데이터 입력 (공백 기준)
# 손님이 입력한 부품별로 있으면 yes 없으면 no 출력

# 입력
# 5
# 8 3 7 9 2
# 3
# 5 7 9

n = int(input())
possession = list(map(int, input().split()))

input_n = int(input())
input_request = list(map(int, input().split()))

possession.sort()


def binary_search_func(data_set, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # 미드는 항상 while scope 안에 그리고 start, end 파라미터로 보내주기
        if data_set[mid] == target:
            return "yes"
        if data_set[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"


for i in range(input_n):
    print(binary_search_func(possession, input_request[i], 0, len(possession) - 1), end=" ")
