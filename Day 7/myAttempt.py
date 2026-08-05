def substring(string):
    sub = ""
    if string == "":
        return 0
    for ch in string:
        if len(sub)>1:
            if ch in sub[0]:
                sub=sub.strip(ch)
                sub+=ch
            elif ch not in sub:
                sub+=ch    
            elif ch in sub[-1]:
                sub = ""
                sub+=ch
        else:
            sub += ch
    return len(sub)

print(substring("abcabcbb"))
print(substring("bbbbb"))
print(substring("pwwkew"))
print(substring(""))