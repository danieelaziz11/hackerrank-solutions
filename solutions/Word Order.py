n = int(input())

words = {}

for _ in range(n):
    word = input()

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(*words.values())