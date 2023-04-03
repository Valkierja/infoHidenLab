from PIL import Image


def hide_data_in_image(img_path, data):
    # 打开图像并将数据嵌入LSB
    img = Image.open(img_path)
    width, height = img.size
    # 将数据编码成二进制字符串
    data_bits = ''.join([format(ord(c), '08b') for c in data])
    # 检查是否有足够的像素容纳数据
    num_pixels = width * height
    if len(data_bits) > num_pixels:
        raise ValueError('Error: Image not large enough to hold data.')
    # 嵌入数据
    data_bits += '0' * (num_pixels - len(data_bits))
    pixel_data = list(img.getdata())
    new_pixel_data = []
    for i, pixel in enumerate(pixel_data):
        if i < len(data_bits):
            new_pixel = (pixel[0], pixel[1], pixel[2], int(format(pixel[3], '08b')[:-1] + data_bits[i], 2))
            new_pixel_data.append(new_pixel)
        else:
            new_pixel_data.append(pixel)
    # 保存带有嵌入数据的新图像
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixel_data)
    new_img.save('hidden.png')


def extract_data_from_image(img_path):
    # 打开图像并从LSB中提取数据
    img = Image.open(img_path)
    pixel_data = list(img.getdata())
    data_bits = ''
    for pixel in pixel_data:
        data_bits += format(pixel[3], '08b')[-1]
    data = ''
    for i in range(0, len(data_bits), 8):
        byte = data_bits[i:i + 8]
        data += chr(int(byte, 2))
        if chr(int(byte, 2)) == '.':
            break
    return data


data_to_hide = "Hello, this is a secret message."
img_path = "input.png"
hide_data_in_image(img_path, data_to_hide)

# 提取数据
extracted_data = extract_data_from_image("hidden.png")
print(extracted_data)
