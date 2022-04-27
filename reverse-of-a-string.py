words = ["Hello", "World"]
for i, word in enumerate(words):
    #word.lower()
    words[i] = word[::-1].lower()

print(words)