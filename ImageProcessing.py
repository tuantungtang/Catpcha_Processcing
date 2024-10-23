import operator

from PIL import Image

im = Image.open("CaptchaImage_test.jpg")
im = im.convert("P")
im2 = Image.new("RGB", im.size, color=(255, 255, 255))
im2 = im2.convert("P")
temp = {}

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        # if pix == 189 or pix == 182 or pix == 66 or pix == 30:  # these are the numbers to get_
        #     im2.putpixel((y, x), 1)
        try:
            temp = (im.getpixel((y, x)) * 10 + im.getpixel((y, x + 1)) + im.getpixel((y, x - 1)) + im.getpixel(
                (y + 1, x)) + im.getpixel(
                (y + 1, x + 1)) + im.getpixel((y + 1, x - 1)) + im.getpixel((y - 1, x)) + im.getpixel(
                (y - 1, x + 1)) + im.getpixel((y - 1, x - 1))) / 9
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


# dien vao cho trong
# def fill_image(im4):
#     for x in range(im4.size[1]):
#         for y in range(im4.size[0]):
#             if
changecaptcha(im2)
im3=im3.convert('RGB')
im3.save("output.jpg")
im2 = im2.convert('RGB')
im2.save("output_image2.jpg")
