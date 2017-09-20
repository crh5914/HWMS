import re
words = {}
def wordCount(file):
	fr = open(file,'r')
	contents = fr.readlines()
	for line in contents:
		words = findWords(line.strip())
		for word in words:
			addWord(word)
def findWords(sentence):
	return re.findall('\w+',sentence)
def addWord(word):
	#print(word)
	words[word] = words.get(word,0) + 1

if __name__ == '__main__':
	wordCount('data.txt')
	print(words)