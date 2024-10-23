import operator

from PIL import Image
from operator import itemgetter

im = Image.open("login_capt.jpg")
im = im.convert("P")
his = im.histogram()

values = {}

for i in range(256):
    values[i] = his[i]

for j,k in sorted(values.items(), key=operator.itemgetter(1), reverse=True)[:10]:
    print (j,k)