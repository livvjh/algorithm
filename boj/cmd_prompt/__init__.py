n = int(input())
root_word = list(input())
for _ in range(n - 1):
    words = input()
    for j in range(len(words)):
        if root_word[j] != words[j]:
            root_word[j] = "?"

print("".join(root_word))
