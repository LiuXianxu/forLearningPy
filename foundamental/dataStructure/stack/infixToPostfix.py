from mystack import Stack
def infixToPostfix(infixexpr): #中缀表达式转后缀表达式
	prec = {"(":1,"+":2,"-":2,"*":3,"/":3}
	opStack = Stack()
	postfixList = []
	tokenList = list(infixexpr)
	#print(tokenList)
	for token in tokenList:
		if token.isalpha() or token.isalnum():
			postfixList.append(token)
		elif token == "(":
			opStack.push(token)
		elif token == ")":
			topToken = opStack.pop()
			while topToken != "(":
				postfixList.append(topToken)  #出栈直到遇到"("
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()]>=prec[token]):
				postfixList.append(opStack.pop())
			opStack.push(token)
	while not opStack.isEmpty():
		postfixList.append(opStack.pop())
	return " ".join(postfixList)
print(infixToPostfix("A*B+C*D"))
print(infixToPostfix("(A+B)*C-(D-E)"))
print(infixToPostfix("A+B*C"))
