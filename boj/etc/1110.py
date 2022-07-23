n = int(input())
count = 0
temp_n = n
if 0 <= int(n) and int(n) <= 99:
    while True:
        sum_value = (temp_n // 10) + (temp_n % 10)
        calculate_value = ((temp_n % 10) * 10) + (sum_value % 10)
        count += 1
        if n == calculate_value:
            break
        temp_n = calculate_value

print(count)
