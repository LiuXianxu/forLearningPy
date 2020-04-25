#import sys
#sys.path.append(r'/home/enmu/Desktop/forLearningPy/foundamental/dataStructure/stack')
from mystack import Stack

def parChecker(symbolString): #括号匹配,全是括号的。。。
	s = Stack()
	#balanced = True
	index = 0
	while index < len(symbolString):
		symbol = symbolString[index]
		if symbol == '(':
			s.push(symbol)
		elif symbol == ')':
			if not s.isEmpty():
				s.pop()
			else :
				return False
		index +=1
	if  s.isEmpty():
		return True
	else :
		return False
print(parChecker('(sdas0)(sdaks;d)(dsada)((()))))ds9a'))
print(parChecker('(123(2((123)))))((3((3))))4(((5(6))))7((8((()9)))0)()'))
print(parChecker("(1)2(2)2(2)"))