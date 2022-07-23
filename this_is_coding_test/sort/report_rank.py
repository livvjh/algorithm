"""
Quiz. 성적이 낮은 순으로 학생들 출력하기(n명의 학생들의 이름과 성적의 정보가 주어졌을때 낮은 순서대로 정렬)
Page. 180
"""
# 입력 (출력 -> 이순신 홍길동)
# 2
# 홍길동 95
# 이순신 88

n = int(input())


def get_sort_key(data):
    return data[1]


student = []
for i in range(n):
    student.append(input().split())

sorted_student_set = sorted(student, key=get_sort_key)

for student in sorted_student_set:
    print(student[0], end=" ")

# 답안 풀이
# n = int(input())
#
# student = []
# for i in range(n):
#     input_value = input().split()
#     student.append((input_value[0], int(input_value[len(input_value) - 1])))
#
# sorted_student_set = sorted(student, key=lambda student: student[1])
# for student in sorted_student_set:
#     print(student[0], end=" ")
