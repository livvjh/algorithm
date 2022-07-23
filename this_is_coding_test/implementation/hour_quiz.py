"""
Quiz. 시각 (주어진 시각 N이 입력으로 주어지면 N시 59분 59초까지 3이 하나라도 포함되는지 찾기)
Page. 113
"""
import time

# 내 코드
n = int(input())
start_time = time.time()
# n시 59분 59초

count = 0
# 00:00:00
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(k) + str(j) + str(i):
                count += 1

print(count)

end_time = time.time()
print(f"소요시간 : {end_time - start_time:.5f} sec")
