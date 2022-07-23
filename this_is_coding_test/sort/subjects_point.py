lenght = int(input())

students = []
for _ in range(lenght):
    students.append(input().split())
# -를 쓰면 역순 (내림차순)
students.sort(
    key=lambda x: (
        -int(x[1]), int(x[2]), -int(x[3]), x[0]  # 1성적 내림차순, 2성적 오름차순, 3성적 내림차순, 4이름 가나다순
    )
)
print(students)

# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90
