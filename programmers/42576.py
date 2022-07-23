# 완주하지 못한 선수

def solution(participant, completion):
    duplication_check_dict = {}
    # 중복 검증을 위한 dict key: value(count)
    for p in participant:
        if duplication_check_dict.get(p):
            duplication_check_dict[p] += 1
        else:
            duplication_check_dict[p] = 1
    # 완주한 리스트 데이터 제거
    for c in completion:
        if duplication_check_dict[c]:
            duplication_check_dict[c] -= 1
    # 무조건 답은 1개이기에 값이 1인 key 리턴
    for key, val in duplication_check_dict.items():
        if val > 0:
            return key


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
