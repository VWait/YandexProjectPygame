from abstractblock import Block


class Board(Block):
    def __init__(self, size, x0, y0, prop_x, prop_y):
        super().__init__(size, x0, y0, prop_x, prop_y)
        self.color = (0, 60, 0)

    def render(self, screen):
        super().render(screen)
