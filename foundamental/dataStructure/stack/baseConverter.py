from mystack import Stack
def baseConverter(decNum,base=2):   #十进制转化为任意进制（十六进制以下）
	digits = "0123456789ABCDEF"		#枚举
	remStack = Stack()
	while decNum > 0:
		remStack.push(decNum % base)
		decNum //= base
	binStr = ""
	while not remStack.isEmpty():
		binStr += digits[remStack.pop()]
	return binStr
print(baseConverter(13,16))