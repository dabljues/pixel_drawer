from drawing_utils.drawer import draw
from image.scraper import scrap_image


def main():
    max_size = (500, 500)
    img = scrap_image('../data/image1.jpg', max_size)
    draw(img)


if __name__ == '__main__':
    main()
