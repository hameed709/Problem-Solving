def Longest_Word(sentence):
    words = sentence.split()
    largest = None
    word_index = None

    for word in words:
        if largest is None:
            largest = len(word)
            word_index = words.index(word)
        if len(word) > largest:
            largest = len(word)
            word_index = words.index(word)
    return words[word_index]

sen = input()
print(Longest_Word(sen))