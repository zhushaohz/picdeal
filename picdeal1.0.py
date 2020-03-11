from PIL import Image
from PIL import ImageFilter
im = Image.open("tjx.jpg")
om = im.filter(ImageFilter.CONTOUR)

om.save('tt.jpg')