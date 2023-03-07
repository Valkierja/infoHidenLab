# 这是一个示例 Python 脚本。
import PIL
from PIL import Image, ImageFilter
from skimage.metrics import mean_squared_error as compare_mse
from skimage.metrics import peak_signal_noise_ratio as compare_psnr
import cv2


def openImg():
    img = Image.open("test.png")
    print(img.size)
    return img


def cropImg(img):
    cropped = img.crop((0, 0, 256, 256))
    newsize = (512, 512)

    im1 = cropped.resize(newsize)
    im1.save("./test_result1.png")


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

def print_psnr_and_mse(img1: Image, img2: Image):
    psnr = compare_psnr(img1, img2)
    mse = compare_mse(img1, img2)

    print('PSNR：{}，MSE：{}'.format(psnr, mse))


if __name__ == "__main__":
    img = openImg()
    cropImg(img)
    rotateImg(img)
    # addNoise(img)
    addFilter(img)
    img = cv2.imread("test.png")
    img2 = cv2.imread("./test_result1.png")
    img3 = cv2.imread("./test_result2.png")
    img4 = cv2.imread("imagetext.png")
    print_psnr_and_mse(img, img2)
    print_psnr_and_mse(img, img3)
    print_psnr_and_mse(img, img4)
