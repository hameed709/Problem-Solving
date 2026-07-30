text = input().lower()
count = 0
temp = None
length = len(text)

for i in range(length):
    for j in range(length):
        if temp is None:
            temp = text[i]
        if temp == text[j]:
            count +=1

    if count != 1:
        count = 0
        temp = None
    else:
        break

if temp is None:
    print("No Non-Repeating Character")
else:
    print(temp)