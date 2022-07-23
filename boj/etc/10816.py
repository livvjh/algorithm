"""
   종류: 해시맵
   접근방식:
   1. input으로 값을 받을때 값을 key로 해당 데이터의 갯수를 value값으로 받는다.
   2. 확인하고자 하는 데이터의 값만큼 반복을 돌며 map에 key값을 조회한다.
   3. 있으면 해당 value값을, 없으면 0을 리스트에 추가 후 리스트 출력
   소요시간: O(n)
"""

n = int(input())

temp_dic = dict()
for key in input().split():
    if temp_dic.get(key) is not None:
        temp_dic[key] += 1
    else:
        temp_dic[key] = 1

given_n = int(input())
result = []
for key in input().split():
    if temp_dic.get(key) is not None:
        result.append(temp_dic[key])
    else:
        result.append(0)

print(*result)
