from PIL import Image


class MBSImage:

    __image = None

    def __init__(self, mbs_object, color_object):
        im = Image.new('RGB', (mbs_object.get_resolution() + 1, mbs_object.get_resolution() + 1))
        if color_object.get_palette_name() == 'wiki':
            color_graph = mbs_object.get_iteration_set() % (color_object.get_num_colors() - 1)
            for x in range(mbs_object.get_resolution() + 1):
                for y in range(mbs_object.get_resolution() + 1):
                    if mbs_object.get_iteration_set()[x][y] == mbs_object.get_max_iter():
                        color_graph[x][y] = 16
        elif color_object.get_palette_name() == 'colorful':
            color_graph = mbs_object.get_iteration_set() % (color_object.get_num_colors() - 1)
            for x in range(mbs_object.get_resolution() + 1):
                for y in range(mbs_object.get_resolution() + 1):
                    if mbs_object.get_iteration_set()[x][y] == mbs_object.get_max_iter():
                        color_graph[x][y] = 1532
        else:
            color_graph = mbs_object.get_iteration_set() % color_object.get_num_colors()
        for x in range(mbs_object.get_resolution() + 1):
            for y in range(mbs_object.get_resolution() + 1):
                im.putpixel((x, y), tuple(color_object.get_palette()[(color_graph[x][y])][:]))
        self.__image = im

    def get_image(self):
        return self.__image
