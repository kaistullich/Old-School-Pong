class Paddle:
    """
    Class for creating the Paddles inside of the Pong game.
    """

    def __init__(self, screen, color, rect, width=0):
        """
        Initializes a pygame rectangle

        :param screen: the surface on which to draw the rectangle

        :param color:  the color the rectangle should be. Needs to be
                       RGB color. ( i.e. BLUE = (0, 0, 255) )

        :param rect:   the location where the rectangle should be drawn,
                       this is a `list` with coordinates [x1, y1, x2, y2]

        :param width:  the width of the border around the rectangle, the
                       the default will be set to 0 so the entire rectangle
                       will be filled in with the color given.
        """
        self.screen = screen
        self.color = color
        self.rect = rect
        self.width = width

    def draw_rect(self, game):
        """
        Draws the actual pygame rectangle

        :param game: the pygame library
        """
        self.game = game
        self.game.draw.rect(self.screen, self.color, self.rect, self.width)
