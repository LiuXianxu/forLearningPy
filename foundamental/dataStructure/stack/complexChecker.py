from mystack import Stack
def parChecker(symbolString):
	s = Stack()
	index = 0
	front = ('{','[','(')
	rear = ('}',']',')')
	while index < len(symbolString):
		symbol = symbolString[index]
		if symbol in front :
			s.push(symbol)
		elif symbol in rear:
			if not s.isEmpty():
				if front.index(s.peek()) == rear.index(symbol) :#  匹配
					s.pop()
				else :
					return False
			else:
				return False
		index += 1

	if s.isEmpty():
		return True
	else :
		return False
#print(parChecker('(sdas0)(sdaks;d)(dsada)((()))))ds9a'))
#print(parChecker('(123(2((123)))))((3((3))))4(((5(6))))7((8((()9)))0)()'))
print(parChecker("12(1)2{()}0{(2)[2]()}2()"))