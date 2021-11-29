# This program is meant to display the mandelbrot set at a particular resolution with given parameters
import sys
import numpy


class MandelbrotSet:
    __max_iter = 1000
    __graph = None
    __zoom = 1
    __resolution = 1000
    __x = 0
    __y = 0

    def __init__(self, x, y, resolution, zoom, max_iter):
        self.__max = 2
        self.__x = x
        self.__y = y
        self.__resolution = resolution
        self.__zoom = zoom
        self.__resolution = resolution
        self.__max_iter = max_iter
        if max_iter > 1000:
            sys.setrecursionlimit(self.__max_iter + 1)
        self.__set_iteration_set()

    @staticmethod
    def out_of_bounds(z, max_iteration):
        c = z
        graph = numpy.ones(c.shape, dtype=int)
        for n in range(max_iteration):
            graph = (numpy.absolute(z) > 2) + graph
            z[numpy.absolute(z) > 2] = 2.1
            z = numpy.multiply(z, z) + c
        return graph

    @staticmethod
    def out_of_bounds2(z, c, graph, bool_graph, max_iteration):
        while numpy.max(graph) != max_iteration and numpy.any(bool_graph):
            z = numpy.multiply(z, z) + c
            z[numpy.absolute(z) > 2] = 2.1
            bool_graph[bool_graph] = numpy.absolute(z[bool_graph]) <= 2
            graph[bool_graph] += 1
        return graph

    def __set_iteration_set(self):
        initial_range = numpy.arange(-2, 2 + 1 / self.get_resolution(), 1 / self.get_resolution() * 4)
        initial_range = initial_range * self.get_zoom()
        real_num = initial_range + self.get_x()
        im_num = initial_range + self.get_y()
        rr, ii = numpy.meshgrid(real_num, im_num)
        grid = rr + ii*1j
        graph = self.out_of_bounds2(grid, grid, numpy.ones(grid.shape, dtype=int), numpy.ones(grid.shape, dtype=bool),
                                    self.get_max_iter())
        #graph = self.out_of_bounds(grid, self.get_max_iter())
        self.__graph = graph
        return

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_zoom(self):
        return self.__zoom

    def get_resolution(self):
        return self.__resolution

    def get_iteration_set(self):
        return self.__graph

    def get_max_iter(self):
        return self.__max_iter

