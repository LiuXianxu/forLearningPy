#import os
with open('sample.txt') as fobj:
	for line in fobj:
		print(line,end='')
#在实际情况中，我们应该尝试使用 with 语句
#处理文件对象，它会在文件用完后会自动关闭，
#就算发生异常也没关系。它是 try-finally 块的简写
with open('sample.txt') as fobj:
	tabs =0
	spaces = 0
	for i,line in enumerate(fobj):
		tabs += line.count('\t')
		spaces += line.count(' ')
	print("Spaces {}. tabs	{}. lines {}".format(spaces,tabs,i+1))
	print(spaces,tabs,i+1)
