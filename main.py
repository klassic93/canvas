from fileparser.parser import *

# Create new empty file
file = open("output.txt", 'w')

# Create "global" variable for our canvas
canvas = None

# Give input.txt and get list with figures and commands
making = get_making("input.txt")

# If we don`t have canvas, finish program
if not isinstance(making[0], Canvas):
    exit()
else:
    # If we have we can continue and write its to file
    canvas = making.pop(0)
    file.write(canvas.show())

# Here we will check our figures in list
for figure_or_dosmth in making:

    # All commands we will write to dict
    # If it is not dict it is figure and we can draw its
    if not isinstance(figure_or_dosmth, dict):
        canvas.draw(figure_or_dosmth, figure_or_dosmth.get_figure())

    # If it is type of dict it is command
    elif isinstance(figure_or_dosmth, dict):
        # If it is fill.. so
        if figure_or_dosmth['do'] == 'fill':
            canvas.fill(figure_or_dosmth['x'], figure_or_dosmth['y'], figure_or_dosmth['color'])

    # Each iteration we will write each figure or command to file
    file.write(canvas.show())

file.close()
