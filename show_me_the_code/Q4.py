#iPhone5->1136*640
import os
from PIL import Image
def listImages(folder):
	files = os.listdir(folder)
	for file in files:
		name = file[:file.rfind('.')]
		ext = file[file.rfind('.')+1:]
		im = Image.open('%s/%s'%(folder,file))
		newSize = getSize(im.size)
		im = im.resize(newSize)
		im.save('%s/%s_rsize.%s'%(folder,name,ext))
def getSize(oldSize):
	widthRatio = 1136/oldSize[0]
	heightRatio = 640/oldSize[1]
	if widthRatio >= 1 and heightRatio >= 1:
		return oldSize 
	if widthRatio < heightRatio:
		return (1136,int(oldSize[1]*widthRatio))
	else:
		return (int(oldSize[0]*heightRatio),640)
if __name__ == '__main__':
	listImages('./images')