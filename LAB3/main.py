import cv2
import numpy as np

# 加载图像
img = cv2.imread('image.png')

# 计算图像像素总数
height, width, channels = img.shape
pixels = height * width

# 生成随机数种子
np.random.seed(1)

# 随机交换像素
for i in range(pixels):
    x1 = np.random.randint(0, width)
    y1 = np.random.randint(0, height)
    x2 = np.random.randint(0, width)
    y2 = np.random.randint(0, height)

    # 交换像素
    temp = img[y1,x1].copy()
    img[y1,x1] = img[y2,x2]
    img[y2,x2] = temp

# 保存置乱后的图像
cv2.imwrite('image_scrambled.jpg', img)

