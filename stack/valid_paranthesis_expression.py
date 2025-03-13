def match_paranthesis(s):
    stack = []
    for x in s:
        if x in ['(', '{', '[']:
            stack.append(x)
        else:
            if len(stack) == 0:
                return False

            z = stack.pop()
            if x == ']' and z != '[':
                return False
            if x == '}' and z != '{':
                return False
            if x == ')' and z != '(':
                return False

    return len(stack) == 0

#End conditions
#What if the there are elements left in the stack
#What if the stack is empty before the elements in the string
#Time complexity: O(n)
#Space complexity: O(n) k is number of opening brackets
s = '([]{})'
print(match_paranthesis(s))

s = '([]{)}'
print(match_paranthesis(s))

s = '([](()))}'
print(match_paranthesis(s))