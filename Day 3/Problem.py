def removeDuplicates(text):
    letters = {}

    for ch in text:
        if ch in letters:
            letters[ch]+=1
        else:
            letters[ch]=1
    return letters.keys()

word = input().lower()
unique = removeDuplicates(word)
result = "".join(unique)
print(result)
