# d(75) = 75 + 7 + 5 => 87

"""
    셀프넘버
    접근방식: 전체리스트와 제거해야할 리스트를 구해서 차집합을 통해 결과도출
"""

natural_num_list = [i for i in range(1, 10001)]
remove_num_list = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    remove_num_list.add(i)

for i in sorted(set(natural_num_list) - remove_num_list):
    print(i)
