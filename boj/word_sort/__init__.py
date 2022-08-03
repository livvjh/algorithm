temp_words = []
for _ in range(int(input())):
    temp_words.append(input())

result = list(set(temp_words))
result.sort(key=lambda x: (len(x), x))
print("\n".join(result))
