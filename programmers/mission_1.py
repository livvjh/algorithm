import datetime
from datetime import timedelta


def solution(booked, unbooked):
    answer = []

    # 2가지 조건이 있다
    def conversion(data):
        temp_time = datetime.datetime.strptime(data, '%H:%M') + timedelta(minutes=10)
        if temp_time.minute < 10:
            return f'{temp_time.hour}:{str(temp_time.minute).zfill(2)}'
        else:
            return f'{temp_time.hour}:{str(temp_time.minute)}'

    def is_bigger_than_10(a, b):
        temp_a = datetime.datetime.strptime(a, '%H:%M') + timedelta(minutes=10)
        temp_b = datetime.datetime.strptime(b, '%H:%M') + timedelta(minutes=10)
        result = temp_b.minute - temp_a.minute
        if result > 10:
            print(result)
            return True
        else:
            print(result)
            # 여기면 무적권 booked 먼저
            return False

    demo = booked + unbooked
    demo.sort(key=lambda x: x[0])
    print(demo)
    print(booked)

    # 어차피 10분 이상 차이 안나면 순서 부킹 먼저 상관없음
    # 그러니 dict에는 booked 애들만 넣고 10분이상 차이나면 이 애들 append 먼저
    temp_dict = {}
    for d in booked:
        temp_dict[d[1]] = d[0]

    for i in range(len(demo)):
        if temp_dict.get(demo[i][1]):
            if demo[i][1] in answer:
                continue
            answer.append(demo[i][1])
        else:
            if len(answer) + 1 == len(demo):
                answer.append(demo[i][1])
                break
            if is_bigger_than_10(demo[i][0], demo[i + 1][0]):
                answer.append(demo[i][1])
            else:
                if len(answer) == 0:
                    answer.append(demo[i][1])
                else:
                    answer.append(demo[i + 1][1])
                    answer.append(demo[i][1])

    # while True:
    #     for key, val in temp_dict.items():
    #         print(key)
    #
    #         if booked[index][1] == key:
    #
    #         print(val)
    # for i in range(len(booked)):
    #     booked_time = conversion(booked[i][0])
    #     if booked_time.minute < 10:
    #         temp_booked.append(f'{booked_time.hour}:{str(booked_time.minute).zfill(2)}')
    #     else:
    #         temp_booked.append(f'{booked_time.hour}:{str(booked_time.minute)}')
    # for i in range(len(temp_booked)):
    #     for j in range(len(temp_unbooked)):
    #         if temp_booked[i] == temp_unbooked[j]:
    #             answer.append(booked[i][1])
    #             break
    #         if temp_booked[i] < temp_unbooked[j]:
    #             if is_bigger_than_10(temp_booked[i], temp_unbooked[j]):
    #                 answer.append(unbooked[j][1])
    #             else:
    #                 answer.append(booked[i][1])
    #         if temp_booked[i] > temp_unbooked[j]:
    #             # 10분 이상 차이나는지 비교
    #             if is_bigger_than_10(temp_booked[i], temp_unbooked[j]):
    #                 answer.append(unbooked[j][1])
    #             else:
    #                 answer.append(booked[i][1])
    #         else:
    #             answer.append(unbooked[j][1])

    #         if booked[i][0] == unbooked[j][0]:
    #             answer.append(booked[i][1])
    #             del temp_booked[i]
    #         if temp_booked[i] < unbooked[j][0]:
    #             answer.append(unbooked[j][1])

    #     print(booked[booked_i][0] > unbooked[unbooked_i][0])
    # print(temp_booked)
    # for i in range(len(booked) + len(unbooked)):
    #     if booked[booked_i][0] == unbooked[unbooked_i][0]:
    #         answer.append(booked[booked_i][1])
    #         booked_i+=1
    #     if booked[booked_i][1]:
    #     print(booked[booked_i][0] > unbooked[unbooked_i][0])
    #     break
    # print(temp_booked)
    # print(temp_unbooked)
    return answer


# print(solution([["09:55", "hae"], ["10:05", "jee"]], [["10:04", "hee"], ["14:07", "eom"]]))
print(solution([["09:10", "lee"]], [["09:00", "kim"], ["09:05", "bae"]]))
