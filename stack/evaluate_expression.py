def evaluate(s):
    stack = []
    current_num = 0
    sign = 1
    result = 0
    for x in s:
        #handles numbers
        if x.isdigit():
            current_num = current_num*10+x
        elif x == '-' or x == '+':
            result += current_num * sign
            sign = -1 if x == '-' else 1
        elif x == '(':
            stack.append(result)
            stack.append(sign)
            sign = 1
            result = 0
        elif x == ')':
            result += current_num*sign
            result += stack.pop()



#Pattern to consider for the stack: if the result of the left elements depend on the rest of the right element.
#if some other elements in the right has to be processed first compared to rest
#precedence matters
s = '18-(7+(2-4))'
print(evaluate(s))