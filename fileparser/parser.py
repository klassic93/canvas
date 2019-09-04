import re
from canvas.canvas import Canvas
from canvas.drawing.drawing import Line
from canvas.drawing.drawing import Rectangle


def __str_handler(str_file):
    """This function will parse str
    """
    making = []
    for line in list(str_file):

        if re.match(r'^(C\s)(\d+\s\d+)$', line):
            params = line.split()
            making.append(Canvas(int(params[1]), int(params[2])))
            continue
        if re.match(r'^(L\s)(\d+\s\d+\s\d+\s\d+)$', line):
            params = line.split()
            making.append(Line(int(params[1]), int(params[2]), int(params[3]), int(params[4])))
            continue
        if re.match(r'^(R\s)(\d+\s\d+\s\d+\s\d+)$', line):
            params = line.split()
            making.append(Rectangle(int(params[1]), int(params[2]), int(params[3]), int(params[4])))
            continue
        if re.match(r'^(B\s)(\d+\s\d+\s\w)$', line):
            params = line.split()
            making.append({"do":"fill", "x":int(params[1]), "y":int(params[2]), "color": params[3]})
            continue

    return making


def __open_file(file_name):
    """This function open file
    end return str file
    """
    file = open(file_name)
    list_file = list(file)
    file.close()
    return list_file


def get_making(file_name):
    str_file = __open_file(file_name)
    return __str_handler(str_file)
