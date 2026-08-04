def group_anagram(List):
    grp={}
    for word in List:
        freq = [0]*26
        for ch in word:
            index = ord(ch)-ord('a')
            if freq[index]!=0:
                freq[index]+=1
            else:
                freq[index]=1
        key = tuple(freq)
        if key not in grp:
            grp[key]=[]
        grp[key].append(word)
    return list(grp.values())

print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagram(["abc", "bca", "cab", "xyz", "zyx"]))
print(group_anagram(["hello"]))