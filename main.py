# 这是一个示例 Python 脚本。
import PIL
from PIL import Image, ImageFilter



def openImg():
    img = Image.open("./test.png")
    print(img.size)
    return img


def cropImg(img):
    cropped = img.crop((512, 512, 1741, 1010))
    cropped.save("./test_result1.png")



def rotateImg(img: PIL.Image):
    rotated = img.rotate(90)
    rotated.save("./test_result2.png")


def addFilter(img: PIL.Image):
    im_result = img.filter(ImageFilter.FIND_EDGES)
    im_result.save('imagetext.png')


# def addNoise(img: PIL.Image):
#     # npised = shimage.util.random_noise(img, mode='gaussian', seed=None, clip=True)
#
#     img1 = Image.new('RGB', (250, 50), color='white')
#     fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
#     d = ImageDraw.Draw(img)
#     d.text((62, 5), "3H1339", font=fnt, fill=(0, 0, 0))
#     img.save('imagetext.png')

if __name__ == "__main__":
    img = openImg()
    cropImg(img)
    rotateImg(img)
    # addNoise(img)
    addFilter(img)
