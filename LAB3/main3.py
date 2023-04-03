from PIL import Image

# 加载图片
img = Image.open('./image.png')
width, height = img.size

# 置乱周期为5
N = 5

for k in range(N):
    img_new = Image.new('RGBA', (width, height))

    for i in range(width):
        for j in range(height):
            x = (2*i + j) % width
            y = (i + j) % height
            img_new.putpixel((x, y), img.getpixel((i, j)))

    img = img_new

# 保存置乱后的图片
img.save('./image_scrambled.png')