"""
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示
请将上述内容写到 student.xls 文件中，如下图所示
"""
import xlwt
import codecs
def dict2xls(dict,file):
	wb = xlwt.Workbook()
	sh = wb.add_sheet('sheet1')
	for row,val in enumerate(dict):
		slist = dict[val]
		for col,item in enumerate(slist):
			sh.write(row,col,item)
	wb.save(file)
def dict2xlsv1(dict,file):
	wb = xlwt.Workbook()
	sh = wb.add_sheet('sheet1')
	for row,key in enumerate(dict):
		val = dict[key]
		sh.write(row,0,str(key))
		sh.write(row,1,str(val))
	wb.save(file)
def dict2xlsv2(arr,file):
	wb = xlwt.Workbook()
	sh = wb.add_sheet('sheet1')
	for i,row in enumerate(arr):
		for j,col in enumerate(row):
			sh.write(i,j,str(col))
	wb.save(file)
def string2dict(dictStr):
	return eval(dictStr)
def loadDictFile(file):
	with codecs.open(file,'r','utf-8') as fr:
		content = ''.join(fr.readlines())
	return content
if __name__ == '__main__':
	content = loadDictFile('student.txt')
	d = string2dict(content)
	dict2xls(d,'student.xls')
	city = loadDictFile('city.txt')
	cd = string2dict(city)
	dict2xlsv1(cd,'city.xls')
	number = loadDictFile('number.txt')
	arr = string2dict(number)
	dict2xlsv2(arr,'number.xls')