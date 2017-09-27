class Rectangle:

    def __init__(self, screen, coords=None, width=0):
        self.screen = screen
        self.color = (255, 255, 255)
        self.coords = coords
        self.width = width


class Circle:

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.size = 8
        self.color = (255, 255, 255)
