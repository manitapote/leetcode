def evaluate(s):
    stack = []
    current_num = 0
    sign = 1
    result = 0
    for x in s:
        #handles numbers
        if x.isdigit():
            #creats a number
            current_num = current_num*10 + int(x)
        elif x == '-' or x == '+':
            #if sign, assign a sign to the number right to it, sign is always in left
            result += current_num * sign
            sign = -1 if x == '-' else 1
            current_num = 0
        elif x == '(':
            #save the previous number and the sign in between them
            stack.append(result)
            stack.append(sign)
            sign = 1
            result = 0
        elif x == ')':
            # '18-(7+(2-4))'
            #evaluate the current number within ()
            #bring back the previous sign and assign to current number
            #bring back the previous number and calculate the result
            #the calculation is always between two number, no matter how many numbers are in between the brackets or out
            #side
            result += current_num*sign
            result = stack.pop()*result
            result += stack.pop()
            current_num = 0

    return result


#Pattern to consider for the stack: if the result of the left elements depend on the rest of the right element.
#if some other elements in the right has to be processed first compared to rest
#precedence matters
#Time complexity: O(n)
#Space complexity: O(n)
s = '18-(7+(2-4))'
print('Result: ', evaluate(s))
print('True :', 18 - (7 + (2-4)))