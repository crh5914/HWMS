#一个HTML文件，找出里面的正文。
import re
import codecs
pattern = '<body>(.*)</body>'
def extractBody(content):
	print(content)
	res = re.findall(pattern,content,flags=re.M|re.S|re.I)
	#print(res)
	return res
def readHtml(file):
	fr = codecs.open(file,'r','utf-8')
	lines = fr.readlines()
	lines = ''.join(lines)
	fr.close()
	return lines
if __name__ == '__main__':
	content = readHtml('C:/Users/b3435/Desktop/web/templates/index.html')
	body = extractBody(content)
	print(body)