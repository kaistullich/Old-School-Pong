class Rectangle:
    """
    Class for creating the Paddles inside of the Pong game.
    """

    def __init__(self, screen, coords=None, width=0):
        """
        Initializes a pygame rectangle

        :param screen: the surface on which to draw the rectangle

        :param coords: the location where the rectangle should be drawn,
                            this is a `list` with coordinates [x1, y1, width, height]

        :param width:  the width of the border around the rectangle, the
                       the default will be set to 0 so the entire rectangle
                       will be filled in with the color given.
        """
        self.screen = screen
        self.color = (255, 255, 255)
        self.coords = coords
        self.width = width
