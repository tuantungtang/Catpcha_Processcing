from csv import reader
import operator
import easyocr
from PIL import Image
import cv2

blurred = cv2.medianBlur(cv2.imread("CaptchaImage (1).jpg"), 3)
cv2.imwrite("blurred.jpg", blurred)
im = Image.open("blurred.jpg")
im = im.convert("L")
im2 = Image.new("RGB", im.size, color=(255, 255, 255))
im2 = im2.convert("P")
temp = {}
mid_weight = 5
side_weight = 1
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        # if pix == 189 or pix == 182 or pix == 66 or pix == 30:  # these are the numbers to get_
        #     im2.putpixel((y, x), 1)
        try:
            temp = (im.getpixel((y, x)) * mid_weight+ (im.getpixel((y, x + 1)) + im.getpixel((y, x - 1)) + im.getpixel(
                (y + 1, x)) + im.getpixel(
                (y + 1, x + 1)) + im.getpixel((y + 1, x - 1)) + im.getpixel((y - 1, x)) + im.getpixel(
                (y - 1, x + 1)) + im.getpixel((y - 1, x - 1)))*side_weight) / 9
            temp = int(temp)
        except:
            temp = 0
        im2.putpixel((y, x), temp)

im3 = Image.new("RGB", im.size, color=(255, 255, 255))
im3 = im3.convert("P")


def changecaptcha(im4):
    for x in range(im4.size[1]):
        for y in range(im4.size[0]):
            if im4.getpixel((y, x)) > 220:
                im3.putpixel((y, x), 225)
            else:
                im3.putpixel((y, x), 0)

changecaptcha(im2)
im3=im3.convert('RGB')
im3.save("output.jpg")
im2 = im2.convert('RGB')
im2.save("output_image2.jpg")
reader = easyocr.Reader(['en'])
result = reader.readtext('output.jpg')
for (box,text,confidence) in result:
    print(f"Detected text: {text} with confidence: {confidence}")
#xc6v
