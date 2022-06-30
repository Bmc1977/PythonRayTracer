from image import Image
from color import Color


def main():
    WIDTH, HEIGHT = 3, 2
    im = Image(WIDTH, HEIGHT)
    red = Color(1, 0, 0)
    green = Color(0, 1, 0)
    blue = Color(0, 0, 1)
    im.setPixel(0, 0, red)
    im.setPixel(1, 0, green)
    im.setPixel(2, 0, blue)

    im.setPixel(0, 1, red + green)
    im.setPixel(1, 1, green + blue + green)
    im.setPixel(2, 1, red * 0.001)

    with open("../test.ppm", "w") as imgFile:
        im.write_ppm(imgFile)


if __name__ == '__main__':
    main()
