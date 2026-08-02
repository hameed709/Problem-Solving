def LongestPrefix(List):
    if len(List)==1:
        print(List[0])
    else:
        first=List[0]
        second=List[1]
        result = common = ""
        for i in range(min(len(first),len(second))):
            if first[i]==second[i]:
                common += first[i]
            else:
                break

        if len(common)>0:
            for ch in List[2:]:
                for i in range(min(len(common),len(ch))):
                    if ch[i]==common[i]:
                        result += ch[i]
                    else:
                        common=result
                        break
                    if common=="":
                        break   
    return common

List1=["flower", "flow", "flight"]
List2=["dog", "racecar", "car"]
List3=["interview", "internet", "internal"]
print(LongestPrefix(List1))
print(LongestPrefix(List2))
print(LongestPrefix(List3))
