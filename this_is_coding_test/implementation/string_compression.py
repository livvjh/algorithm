# 문자열 압축

input_value = input()


def compression_count(s):
    length = len(s)
    # 절반만 확인하면 돼 리스트의 절반 이후는 쪼갠 앞뒤의 갯수가 맞지 않음
    # 8 => 4, 0,1,2,3
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):  # (시작값, 반복길이, 증가수) 1, 4, 2 => 2번 반복한다는 의미
            if prev == s[j: j + step]:  # step = 1 -> [0:1] == [1:2] 앞숫자와 비교 step = 2 -> [0:2] == [2:4]
                count += 1
            else:
                # 삼항연산자 "참 -> str(count) + prev " if 조건 else "거짓" -> prev
                # count 2보다 같거나 크다는 말은 앞뒤 숫자가 연속헀다는 의미 이때 갯수를 함께 compressed에 저장 아니면 prev 알파벳만 저장
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j: j + step]  # 다음으로 넘기기 0:1 -> 1:2
                count = 1  # count 초기화
        compressed += str(count) + prev if count >= 2 else prev  # 남아 있는 문자열 마지막 처리
        length = min(length, len(compressed))  # 그냥 길이와 압축한 길이 비교해서 더 짧은것 return
    return length


print(compression_count(input_value))
