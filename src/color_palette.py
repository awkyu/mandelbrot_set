import numpy
import array as arr


class Colors:

    __color_palettes = None
    __num_colors_palettes = None
    __chosen = None
    __num_colors = None
    __palette_name = None

    def __init__(self, chosen_palette):
        self.__palette_name = chosen_palette
        self.__color_palettes = {'ncsu': Colors.ncsu(), 'wiki': Colors.wiki(), 'ice': Colors.ice(),
                                 'fire': Colors.fire(), 'colorful': Colors.colorful(), 'bluegreen': Colors.bluegreen()}
        self.__num_colors_palettes = {'ncsu': 21, 'wiki': 16, 'ice': 21, 'fire': 22, 'colorful': 1532,
                                      'bluegreen': 1022}
        self.__chosen = self.__color_palettes[chosen_palette]
        self.__num_colors = self.__num_colors_palettes[chosen_palette]

    def get_palette(self):
        return self.__chosen

    def get_num_colors(self):
        return self.__num_colors

    def get_palette_name(self):
        return self.__palette_name

    @staticmethod
    def ncsu():
        ncsu_color = numpy.empty([21, 3], dtype=int)
        ncsu_color[0][:] = arr.array('i', [255, 255, 255])
        ncsu_color[1][:] = arr.array('i', [255, 204, 204])
        ncsu_color[2][:] = arr.array('i', [255, 153, 153])
        ncsu_color[3][:] = arr.array('i', [255, 102, 102])
        ncsu_color[4][:] = arr.array('i', [255, 51, 51])
        ncsu_color[5][:] = arr.array('i', [255, 0, 0])
        ncsu_color[6][:] = arr.array('i', [204, 0, 0])
        ncsu_color[7][:] = arr.array('i', [153, 0, 0])
        ncsu_color[8][:] = arr.array('i', [102, 0, 0])
        ncsu_color[9][:] = arr.array('i', [51, 0, 0])
        ncsu_color[10][:] = arr.array('i', [0, 0, 0])
        ncsu_color[20][:] = arr.array('i', [255, 255, 255])
        ncsu_color[19][:] = arr.array('i', [255, 204, 204])
        ncsu_color[18][:] = arr.array('i', [255, 153, 153])
        ncsu_color[17][:] = arr.array('i', [255, 102, 102])
        ncsu_color[16][:] = arr.array('i', [255, 51, 51])
        ncsu_color[15][:] = arr.array('i', [255, 0, 0])
        ncsu_color[14][:] = arr.array('i', [204, 0, 0])
        ncsu_color[13][:] = arr.array('i', [153, 0, 0])
        ncsu_color[12][:] = arr.array('i', [102, 0, 0])
        ncsu_color[11][:] = arr.array('i', [51, 0, 0])
        return ncsu_color

    @staticmethod
    def wiki():
        wiki_color = numpy.empty([17, 3], dtype=int)
        wiki_color[0][:] = arr.array('i', [66, 30, 15])
        wiki_color[1][:] = arr.array('i', [25, 7, 26])
        wiki_color[2][:] = arr.array('i', [9, 1, 47])
        wiki_color[3][:] = arr.array('i', [4, 4, 73])
        wiki_color[4][:] = arr.array('i', [0, 7, 100])
        wiki_color[5][:] = arr.array('i', [12, 44, 138])
        wiki_color[6][:] = arr.array('i', [24, 82, 177])
        wiki_color[7][:] = arr.array('i', [57, 125, 209])
        wiki_color[8][:] = arr.array('i', [134, 181, 229])
        wiki_color[9][:] = arr.array('i', [211, 236, 248])
        wiki_color[10][:] = arr.array('i', [241, 233, 191])
        wiki_color[11][:] = arr.array('i', [248, 201, 95])
        wiki_color[12][:] = arr.array('i', [255, 170, 0])
        wiki_color[13][:] = arr.array('i', [204, 128, 0])
        wiki_color[14][:] = arr.array('i', [153, 87, 0])
        wiki_color[15][:] = arr.array('i', [106, 52, 3])
        wiki_color[16][:] = arr.array('i', [0, 0, 0])
        return wiki_color

    @staticmethod
    def ice():
        ice_color = numpy.empty([21, 3], dtype=int)
        ice_color[0][:] = arr.array('i', [255, 255, 255])
        ice_color[1][:] = arr.array('i', [204, 255, 255])
        ice_color[2][:] = arr.array('i', [102, 255, 255])
        ice_color[3][:] = arr.array('i', [0, 255, 255])
        ice_color[4][:] = arr.array('i', [51, 204, 255])
        ice_color[5][:] = arr.array('i', [0, 153, 255])
        ice_color[6][:] = arr.array('i', [0, 102, 255])
        ice_color[7][:] = arr.array('i', [0, 0, 255])
        ice_color[8][:] = arr.array('i', [0, 0, 204])
        ice_color[9][:] = arr.array('i', [0, 0, 102])
        ice_color[10][:] = arr.array('i', [0, 0, 0])
        ice_color[20][:] = arr.array('i', [255, 255, 255])
        ice_color[19][:] = arr.array('i', [204, 255, 255])
        ice_color[18][:] = arr.array('i', [102, 255, 255])
        ice_color[17][:] = arr.array('i', [0, 255, 255])
        ice_color[16][:] = arr.array('i', [51, 204, 255])
        ice_color[15][:] = arr.array('i', [0, 153, 255])
        ice_color[14][:] = arr.array('i', [0, 102, 255])
        ice_color[13][:] = arr.array('i', [0, 0, 255])
        ice_color[12][:] = arr.array('i', [0, 0, 204])
        ice_color[11][:] = arr.array('i', [0, 0, 102])
        return ice_color

    @staticmethod
    def fire():
        fire_color = numpy.empty([22, 3], dtype=int)
        fire_color[0][:] = arr.array('i', [255, 255, 255])
        fire_color[1][:] = arr.array('i', [255, 255, 204])
        fire_color[2][:] = arr.array('i', [255, 255, 153])
        fire_color[3][:] = arr.array('i', [255, 255, 102])
        fire_color[4][:] = arr.array('i', [255, 255, 0])
        fire_color[5][:] = arr.array('i', [255, 204, 0])
        fire_color[6][:] = arr.array('i', [255, 153, 51])
        fire_color[7][:] = arr.array('i', [255, 102, 0])
        fire_color[8][:] = arr.array('i', [255, 51, 0])
        fire_color[9][:] = arr.array('i', [255, 0, 0])
        fire_color[10][:] = arr.array('i', [128, 0, 0])
        fire_color[11][:] = arr.array('i', [0, 0, 0])
        fire_color[21][:] = arr.array('i', [255, 255, 255])
        fire_color[20][:] = arr.array('i', [255, 255, 204])
        fire_color[19][:] = arr.array('i', [255, 255, 153])
        fire_color[18][:] = arr.array('i', [255, 255, 102])
        fire_color[17][:] = arr.array('i', [255, 255, 0])
        fire_color[16][:] = arr.array('i', [255, 204, 0])
        fire_color[15][:] = arr.array('i', [255, 153, 51])
        fire_color[14][:] = arr.array('i', [255, 102, 0])
        fire_color[13][:] = arr.array('i', [255, 51, 0])
        fire_color[12][:] = arr.array('i', [255, 0, 0])
        fire_color[11][:] = arr.array('i', [128, 0, 0])
        return fire_color

    @staticmethod
    def colorful():
        colorful_color = numpy.empty([1533, 3], dtype=int)
        colorful_color[:][:] = 0
        colorful_color[0:255][0] = 255
        colorful_color[1276:1530][0] = 255
        for r in range(255, -1):
            colorful_color[256 + 255 - r][0] = r
        for r in range(0, 256):
            colorful_color[1021 + r][0] = r
        for g in range(0, 256):
            colorful_color[0 + g][1] = g
        colorful_color[256:766][1] = 255
        for g in range(255, -1):
            colorful_color[766 + 255 - g][1] = g
        for b in range(0, 256):
            colorful_color[510 + b][2] = b
        colorful_color[766:1275][2] = 255
        for b in range(255, -1):
            colorful_color[1276 + 255 - b][2] = b
        colorful_color[1532][:] = arr.array('i', [0, 0, 0])
        return colorful_color

    @staticmethod
    def bluegreen():
        bluegreen_color = numpy.empty([1022, 3], dtype=int)
        bluegreen_color[:][:] = 0
        for b1 in range(0, 256):
            bluegreen_color[b1, 2] = b1
        bluegreen_color[256:510, 2] = 255
        for g1 in range(0, 256):
            bluegreen_color[256 + g1, 1] = g1
        for b2 in range(255, -1):
            bluegreen_color[511 + 255 - b2, 2] = b2
        for g2 in range(255, -1):
            bluegreen_color[766 + 255 - g2, 1] = g2
        bluegreen_color[511:765, 1] = 255
        bluegreen_color[:, 0] = 0
        return bluegreen_color
