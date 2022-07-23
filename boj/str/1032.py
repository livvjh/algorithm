"""
   종류: 문자열
   접근방식:
   1. 첫번쨰 데이터를 기준으로 문자열을 리스트로 반환 (추후 값을 ? 로 바꾸기 위함)
   2. 2번쨰 입력데이터와 비교하며 같지 않을때 해당 첫번쨰 데이터 index의 값을 ? 로 변경
   3. list를 join으로 print
"""
n = int(input())
root_word = list(input())
for _ in range(n - 1):
    words = input()
    for j in range(len(words)):
        if root_word[j] != words[j]:
            root_word[j] = "?"

print("".join(root_word))