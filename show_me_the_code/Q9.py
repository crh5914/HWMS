#一个HTML文件，找出里面的链接
import re
link = '<a\s*href="(.*)">.*</a>'
def extractLinks(content):
	links = re.findall(link,content,flags=re.I|re.M|re.S)
	return links
if __name__ == '__main__':
	print(extractLinks('<a href="www.baidu.com">baidu\r\n</a>'))
