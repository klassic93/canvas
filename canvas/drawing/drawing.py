from abc import *
from ..exceptions.ownerrors import RangeException, RectangleWrong


class Drawing(metaclass=ABCMeta):
    def __init__(self, x1, y1, x2, y2):
        try:
            for point in [x1, y1, x2, y2]:
                if point < 1:
                    raise RangeException()
        except RangeException as e:
            print(e)
        else:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

    @abstractmethod
    def get_coordinates(self):
        return [self.x1, self.y1, self.x2, self.y2]

    @abstractmethod
    def get_figure(self):
        pass


class Line(Drawing):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        if self.y1 == self.y2:
            self.line = self.__draw_horizontal_line()
        elif self.x1 == self.x2:
            self.line = self.__draw_vertical_line()

    def __draw_horizontal_line(self):
        if self.x1 <= self.x2:
            return [[x, self.y2 - 1] for x in range(self.x1 - 1, self.x2)]
        if self.x1 > self.x2:
            return [[x, self.y2 - 1] for x in range(self.x1 - 1, self.x2 - 2, -1)]

    def __draw_vertical_line(self):
        if self.y1 <= self.y2:
            return [[self.x2 - 1, y] for y in range(self.y1 - 1, self.y2)]
        if self.y1 > self.y2:
            return [[self.x2 - 1, y] for y in range(self.y1 - 1, self.y2 - 2, -1)]

    def get_coordinates(self):
        return [self.x1, self.y1, self.x2, self.y2]

    def get_figure(self):
        return self.line


class Rectangle(Line):
    def __init__(self, x1, y1, x2, y2):
        try:
            super().__init__(x1, y1, x2, y2)

            if self.x1 <= self.x2 and self.y1 <= self.y2:
                self.rectangle = self.__draw_rectangle()
            else:
                raise RectangleWrong()
        except RectangleWrong as e:
            print(e)

    def __draw_rectangle(self):
        line_top = Line(self.x1, self.y1, self.x2, self.y1)
        line_bottom = Line(self.x1, self.y2, self.x2, self.y2)
        line_left = Line(self.x1, self.y1, self.x1, self.y2)
        line_right = Line(self.x2, self.y1, self.x2, self.y2)

        lines = []
        lines.extend(line_top.get_figure())
        lines.extend(line_bottom.get_figure())
        lines.extend(line_left.get_figure())
        lines.extend(line_right.get_figure())
        return lines

    def get_figure(self):
        return self.rectangle

    def get_coordinates(self):
        return [self.x1, self.y1, self.x2, self.y2]
