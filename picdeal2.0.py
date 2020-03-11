from PIL import Image
im = Image.open('tjx.jpg')
r,g,b = im.split()
om = Image.merge("RGB",(b,r,g))
pm = Image.blend(im,om,0.5)
pm.save('ttt.jpg')