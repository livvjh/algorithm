"""
   종류: 정렬
   접근방식:
   해당 값의 합을 리턴한다.
   소요시간: O(n)
"""

temp_words = []
for _ in range(int(input())):
    temp_words.append(input())

result = list(set(temp_words))  # 입력된 단어들 중복제거, 리스트 변환

# key에 람다함수를 주고 첫번째 우선순위로 len(x) 길이짧은것 (역순은 -)
# 두번째로 알파벳순 값을 그대로 넣으면 알파벳 순으로 정렬 (sort함수는 문자열도 그대로 정렬해줌)
result.sort(key=lambda x: (len(x), x))
print("\n".join(result))
