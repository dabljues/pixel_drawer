import PIL.Image
import numpy as np


def scrap_image(path: str, max_size: tuple) -> np.array:
    img: PIL.Image.Image = PIL.Image.open(path)
    # Resize the image preserving the aspect ratio
    width, height = img.size
    if (width, height) > max_size:
        width_coeff = max_size[0] / width
        height_coeff = max_size[1] / height
        coeff = min((width_coeff, height_coeff))
        img.thumbnail((width * coeff, height * coeff), PIL.Image.ANTIALIAS)
    img = img.convert('1')
    return np.array(img)
