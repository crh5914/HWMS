#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os
def calcodes(folder):
	codes = {}
	files = os.listdir(folder)
	for file in files:
		fr = open('{}/{}'.format(folder,file),'r')
		lines = fr.readlines()
		flag = False
		for line in lines:
			line = line.strip()
			if not len(line):
				continue
			if line.find('#') == 0:
				codes['comment'] = codes.get('comment',0) + 1
			elif line.find("'''") == 0 and not flag:
				flag = True
				codes['comment'] = codes.get('comment',0) + 1
			elif flag:
				codes['comment'] = codes.get('comment',0) + 1
				if line.rfind("'''")>=0:
					flag = False
			else:
				codes['code'] = codes.get('code',0) + 1
	print(codes)
if __name__ == '__main__':
	calcodes('./code')
