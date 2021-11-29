from src import mandelbrot_set, color_palette, mbs_image
from PIL import Image
import numpy


def main():
    mbs1 = mandelbrot_set.MandelbrotSet(0.267235642726, -0.003347589624, 1000, 1.15E-10, 5000)
    cp1 = color_palette.Colors("wiki")
    image = mbs_image.MBSImage(mbs1, cp1)
    final_image = image.get_image()
    final_image = final_image.transpose(Image.ROTATE_90)
    final_image.save('test.png')


if __name__ == "__main__":
    main()
