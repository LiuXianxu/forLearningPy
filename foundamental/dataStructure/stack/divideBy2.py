from mystack import Stack
def divideBy2(decNum):  
	remStack = Stack()
	while decNum > 0:
		remStack.push(decNum % 2)
		decNum //= 2 
	binStr = ""
	while not remStack.isEmpty():
		binStr += str(remStack.pop())
	return binStr

print(divideBy2(13))