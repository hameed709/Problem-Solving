def ValidParanthesis(string):
    stack = []
    pairs = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for ch in string:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack[-1]!=pairs[ch]:
                return False
            stack.pop()

    return len(stack)==0

print(ValidParanthesis("()"))
print(ValidParanthesis("()[]{}"))
print(ValidParanthesis("(]"))
print(ValidParanthesis("([{}])"))
print(ValidParanthesis("([)]"))