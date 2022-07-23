# 체육복

# 다른 답 - 1
def solution(n, lost, reserve):
    reserves = set(reserve) - set(lost)
    losts = set(lost) - set(reserve)

    for reverse in reserves:
        # 앞번호 먼저
        if reverse - 1 in losts:
            losts.remove(reverse - 1)
        elif reverse + 1 in losts:
            losts.remove(reverse + 1)

    return n - len(losts)


# 내 풀이
# def solution(n, lost, reserve):
#     lost_students = set(lost) - set(reserve)
#     reserve_students = set(reserve) - set(lost)
#     for lost_student in lost_students:
#         if lost_student + 1 in reserve_students:
#             reserve_students.remove(lost_student + 1)
#         elif lost_student - 1 in reserve_students:
#             reserve_students.remove(lost_student - 1)
#         else:
#             n -= 1
#     return n


print(solution(5, [2, 4], [3]))
