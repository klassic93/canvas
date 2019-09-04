class RangeException(Exception):
    def __init__(self):
        print("This value have to more than 0..")


class NotTypeCorrespond(Exception):
    def __init__(self):
        super().__init__("This type doesn`t correspond Canvas type..")

class RectangleWrong(Exception):
    def __init__(self):
        super().__init__("This rectangle is wrong..")
