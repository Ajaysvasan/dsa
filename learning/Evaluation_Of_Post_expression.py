def evaluation(givenExpression):
    stack = []
    for char in givenExpression:
        if char.isdigit():
            stack.append(int(char))
        else:
            topOne = stack.pop()
            topSecond = stack.pop()
            if char=='+':
                stack.append(topOne+topSecond)
            elif char == '-':
                stack.append(topSecond-topOne)
            elif char == "x":
                stack.append(topOne*topSecond)
            elif char == "/":
                stack.append(topSecond//topOne)
            elif char == "%":
                stack.append(topSecond%topOne)
            elif char=="^":
                stack.append(topSecond^topOne)
        print(stack)
    return stack.pop()

print(evaluation( "72/96-8+" ))