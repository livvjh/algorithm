natural_num_list = [i for i in range(1, 10001)]
remove_num_list = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    remove_num_list.add(i)

for i in sorted(set(natural_num_list) - remove_num_list):
    print(i)
