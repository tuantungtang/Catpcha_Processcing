import operator
import easyocr
from PIL import Image
from operator import itemgetter

im = Image.open("login_capt.jpg")
im = im.convert("P")
his = im.histogram()

values = {}
reader = easyocr.Reader(['en'])
result = reader.readtext('output.jpg')
print(result)