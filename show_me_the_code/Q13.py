# xls to xml
import xlrd
import codecs
def xls2dict(file):
	wb = xlrd.open_workbook(file)
	sh = wb.sheet_by_index(0)
	d = {}
	for row in range(sh.nrows):
		key = sh.cell_value(rowx=row,colx=0)
		l = []
		for col in range(sh.ncols):
			if col == 0:
				continue 
			l.append(sh.cell_value(rowx=row,colx=col))
		d[key] = l
	return d
def dict2xml(d):
	print(d)
	fw = codecs.open('student.xml','w','utf-8')
	content = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n<students>\n<!--\n学生信息表\n"id" : [名字, 数学, 语文, 英文]\n-->\n{}\n</students>'.format(str(d))
	fw.write(content)
	fw.close()

if __name__ == '__main__':
	d  = xls2dict('student.xls')
	dict2xml(d)