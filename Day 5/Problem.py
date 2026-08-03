def anagram(s,t):
    freq = {}
    if len(s)!=len(t):
        return False
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for ch in t:
        if ch not in freq:
            return False
        freq[ch]-=1
        if freq[ch]<0:
            return False

    for value in freq.values():
        if value!=0:
            return False
    return True


s = "triangle"
t = "integral"

print(anagram(s,t))