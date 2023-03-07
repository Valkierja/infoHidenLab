from PIL import Image
import random

def generate():

    image = Image.new(mode="RGB", size=(300, 300), color="white")
    image.save("TEST2_white.png")

    black_pixTuple = (0, 0, 0, 0)  ###三个参数依次为R,G,B,A   R：红 G:绿 B:蓝 A:透明度
    for i in range(300):
        for j in range(300):
            image.putpixel((i, j), black_pixTuple)
    image.save("TEST2_white_black.png")

if __name__=="__main__":
    generate()