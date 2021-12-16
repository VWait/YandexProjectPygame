from spriteclass import Sprite


class Card(Sprite):
    def __init__(self, group, file_name, pos0):
        super().__init__(group)
        self.image = self.load_image(file_name)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos0
