from .drawing.drawing import Drawing
from .exceptions.ownerrors import RangeException, NotTypeCorrespond


class Canvas:
    def __init__(self, canvas_width, canvas_height):
        try:
            if canvas_height < 1 or canvas_width < 1:
                raise RangeException()
        except RangeException as e:
            print(e)
        else:
            self.canvas_width = canvas_width
            self.canvas_height = canvas_height
            self.canvas = [[" "] * canvas_width for i in range(canvas_height)]

    def draw(self, figure, points):
        """This function have getting coordinates
        and fill each
        """
        try:
            if not isinstance(figure, Drawing):
                raise NotTypeCorrespond()
        except NotTypeCorrespond as e:
            print(e)
        else:
            if self.__check_size(figure):
                for point in points:
                    self.canvas[point[1]][point[0]] = "x"
            else:
                print("this figure doesn`t fit into the canvas")

    def fill(self, x1, y1, color):
        """Just fill
        """
        x1 -= 1
        y1 -= 1

        # First check on fill "pixel"
        if self.canvas[y1][x1] == "*" or x1 < 0 or y1 < 0:

            # but we should throw some exception..
            return "Error"

        # so here start difficult thing
        first_list = []
        while True:
            self.canvas[y1][x1] = color
            if (x1 + 1) < self.canvas_width and self.canvas[y1][x1 + 1] == " ":
                if not [x1 + 1, y1] in first_list:
                    first_list.append([x1 + 1, y1])
            if (y1 + 1) < self.canvas_height and self.canvas[y1 + 1][x1] == " ":
                if not [x1, y1 + 1] in first_list:
                    first_list.append([x1, y1 + 1])
            if (x1 - 1) >= 0 and self.canvas[y1][x1 - 1] == " ":
                if not [x1 - 1, y1] in first_list:
                    first_list.append([x1 - 1, y1])
            if (y1 - 1) >= 0 and self.canvas[y1 - 1][x1] == " ":
                if not [x1, y1 - 1] in first_list:
                    first_list.append([x1, y1 - 1])
            if len(first_list) <= 0:
                break

            for point in first_list:
                self.canvas[point[1]][point[0]] = color

            remove_elem = first_list.pop(0)
            x1 = remove_elem[0]
            y1 = remove_elem[1]

    def clear(self):
        pass

    def show(self):
        """Return our canvas in string type
        """
        picture = ""
        for ruf in range(self.canvas_width + 2):
            picture += "-"
        picture += "\n"
        for height in range(self.canvas_height):
            picture += "|"
            for width in range(self.canvas_width):
                picture += self.canvas[height][width]
            picture += "|\n"
        for ruf in range(self.canvas_width + 2):
            picture += "-"
        picture += "\n"
        return picture

    def __check_size(self, figure):
        """Checking size our future figure
        """
        if figure.x1 > self.canvas_width or figure.y1 > self.canvas_height:
            return False
        if figure.x2 > self.canvas_width or figure.y2 > self.canvas_height:
            return False
        return True
