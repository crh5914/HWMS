'''
 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
 '''
import jieba
import codecs 
def loadFilteredWords(file):
	fr = codecs.open(file,'r','utf-8')
	words = [word.strip() for word in fr.readlines()]
	return words
def filterWords(input,wordsDict):
	words = jieba.cut(input)
	filtered = []
	flag = False
	for word in words:
		if word in wordsDict:
			filtered.append('*'*len(word))
			flag = True
			continue
		filtered.append(word)
	if flag:
		print('Freedom\n')
	else:
		print('Human Rights\n')
	return ''.join(filtered)
if __name__ == '__main__':
	run = True
	wordsDict = loadFilteredWords('filtered_words.txt')
	print("Enter 'q' to quit.\n")
	while run:
		content = input()
		if content == 'q':
			break
		filtered = filterWords(content,wordsDict)
		print('==========\n{}\n=========='.format(filtered))


