def expand(left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1:right]

def longest_palindrome(s):
    longest = ""

    for i in range(len(s)):

        p1 = expand(i, i, s)
        p2 = expand(i, i + 1, s)

        if len(p1) > len(longest):
            longest = p1

        if len(p2) > len(longest):
            longest = p2
    return longest

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("forgeeksskeegfor"))