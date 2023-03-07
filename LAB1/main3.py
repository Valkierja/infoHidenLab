from PIL import Image


def binary(threshold: int, path: str):
    im = Image.open("test.png")
    # convert to grey level image
    Lim = im.convert("L")
    Lim.save("test_gray.png")

    # threshold = 200
    # threshold = 80

    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    bim = Lim.point(table, "1")
    bim.save(path)


if __name__ == "__main__":
    binary(200, "test_binary1.png")
    binary(80, "test_binary2.png")
