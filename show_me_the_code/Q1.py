from PIL import Image,ImageDraw

im = Image.open("test.jpeg")
print(im.size)
draw = ImageDraw.Draw(im)
draw.text((im.size[0]-50,20),'4',fill=(255,0,0))
# write to stdout
im.save('copy.jpeg', "jpeg")