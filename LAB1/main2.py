from PIL import Image
import random


def loopDraw(img: Image, lower: int, step: int, color: tuple, savePath: str):
    # black_pixTuple = (0, 0, 0, 0)
    for i in range(300):
        for j in range(lower, lower + step):
            img.putpixel((i, j), color)
    img.save(savePath)


def generate_white_black():
    image = Image.new(mode="RGB", size=(300, 300), color="white")
    image.save("TEST2_white.png")
    black_pixTuple = (0, 0, 0, 0)

    # black_pixTuple = (0, 0, 0, 0)
    counter = 0
    step = 0
    step2 = 0

    while (counter + step+step2 <= 300):
        step = random.randint(1, 5)
        loopDraw(image, counter, step, black_pixTuple, "TEST2_white_black.png")
        step2 = random.randint(1, 3)

        counter = counter + step + step2


def generate_Red_Green():
    image = Image.new(mode="RGB", size=(300, 300), color="red")
    image.save("TEST2_red.png")
    green_pixTuple = (0, 255, 0, 0)

    # black_pixTuple = (0, 0, 0, 0)
    counter = 0
    step = 0
    step2=0
    while (counter + step+step2 <= 300):
        step = random.randint(1, 5)
        loopDraw(image, counter, step, green_pixTuple, "TEST2_red_green.png")
        step2 = random.randint(1, 3)
        counter = counter + step + step2


if __name__ == "__main__":
    generate_white_black()
    generate_Red_Green()
