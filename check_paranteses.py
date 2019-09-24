def check_parantheses(s):
    mapping = {'{':'}','[':']','(':')'}
    open = ['{','(','[']
    close = [')',']','}']
    stack = []
    for i in range(0,len(s)):
        if s[i] in open:
            stack.append(s[i])
        if s[i] in close:
            c = mapping[stack.pop()]
            if c!=s[i]:
                return False
    if len(stack)!=0:
        return False
    return True

s1 = "{}"
s2 = "[)"
s3 = "({[)]"
s4 = "{{{}()}[]}"

print(check_parantheses(s1))
print(check_parantheses(s2))
print(check_parantheses(s3))
print(check_parantheses(s4))

    
