import pygame
import math


pygame.font.init()


class Block:
    def __init__(self, pos0, props, parent):
        self.size = tuple(map(lambda x, y: x * y, parent.size, props))
        self.pos0 = pos0
        self.color = (175, 214, 255)
        self.blip_color = (53, 177, 255)

        self.help_size = self.size[0] * 0.25, self.size[1] * 0.1
        self.help_pos0 = self.pos0[0] + 10, self.size[1] - self.help_size[1] - 10
        self.start_size = self.help_size
        self.start_pos0 = self.size[0] - self.help_size[0] - 10, self.help_pos0[1]

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.pos0 + self.size)
#        pygame.draw.rect(screen, self.blip_color, self.help_pos0 + self.help_size)
#        pygame.draw.rect(screen, self.blip_color, self.start_pos0 + self.start_size)

    def get_pos0_by_prop(self, props, size_child):
        return tuple(map(lambda val, p, s: val * p - s / 2, self.size, props, size_child))


class Window:
    def __init__(self):
        self.pos0 = (0, 0)
        self.size = 0


class Board(Block):
    def __init__(self, pos0, props, parent):
        super().__init__(pos0, props, parent)
        distance_border = 40
        hand_size = self.size[0] * 0.4, self.size[1] * 0.3
        point1 = self.pos0[0] + distance_border, self.pos0[1] + distance_border
        point2 = self.size[0] - distance_border - hand_size[0], self.pos0[1] + distance_border
        point3 = self.pos0[0] + self.size[0] / 2 - hand_size[0] / 2, self.pos0[1] + distance_border * 2 + hand_size[1]
        self.slots_points = {'0': point3, '1': point1, '2': point2}
        super().__init__(pos0, props, parent)

    def render(self, screen):
        super(Board, self).render(screen)
        pygame.draw.rect(screen, self.blip_color, self.help_pos0 + self.help_size)
        pygame.draw.rect(screen, self.blip_color, self.start_pos0 + self.start_size)

    def get_hand_by_number(self, slot):
        return PlayerHand(self.slots_points[slot], self)


class PlayerHand(Block):
    def __init__(self, pos0, parent):
        super().__init__(pos0, (0.4, 0.3), parent)
        self.rect = pygame.Rect(pos0 + self.size)
        self.color = (58, 144, 255)
        self.clicked = 0
        self.color_name = (205, 255, 255)
        self.rect_name = self.size[0], self.size[1] / 6
        self.font = pygame.font.SysFont('cambria', 20)
        self.circles = []
        self.radius = 10
        self.now_circle = (0, 0)

    def get_pos0_card(self, n):
        ratio = (3.5, 1.55, 4)
        cards = [(self.pos0[0] + self.size[0] / ratio[i],
                  self.pos0[1] + self.size[1] / ratio[2]) for i in range(1, 3)]
        return cards[n]

    def contour_window(self, screen):
        block_pos0 = self.pos0[0] - 3, self.pos0[1] - 3
        block_size_window = self.size[0] + 6, self.size[1] + 6
        pygame.draw.rect(screen, (255, 255, 255), block_pos0 + block_size_window, width=3)

    def cards_played(self, screen, cards):
        radius = 12.5
        ratio = (6, 5)
        pos0 = (self.rect[0], self.rect[1] + 25)
        count_card = 0
        for i in range(math.ceil(len(cards) / 2)):
            for j in range(2):
                count_card += 1
                x, y = (pos0[0] + (ratio[0] + radius) * (j + 1) + radius * j,
                        pos0[1] + (ratio[1] + radius) * (i + 1) + radius * i)
                pygame.draw.circle(screen, (255, 255, 255), (x, y),
                                   radius, 0)
                text = self.font.render(str(cards[count_card - 1]), True, (0, 0, 255))
                screen.blit(text, (x - 6, y - 12))
                if count_card == len(cards):
                    break

    def choice_cards(self, screen):
        rect = (self.rect[0], self.rect[1] + self.size[1], self.rect[2], self.rect[3] / 5)
        pygame.draw.rect(screen, (150, 180, 255), rect)
        self.circles = []
        for i in range(7):
            self.circles.append((rect[2] / 7 * i + rect[0] + self.radius * 2, self.rect[3] + self.rect[1] + rect[3] / 2))
            pygame.draw.circle(screen, (0, 255, 255), self.circles[i], self.radius, 0)
            text = self.font.render(str(i + 1), True, (30, 30, 255))
            screen.blit(text, (self.circles[i][0] - 5, self.circles[i][1] - 12))

    def contour_circle(self, xy, screen):
        pygame.draw.circle(screen, (255, 255, 255), xy, self.radius + 3, width=3)

    def render(self, screen, name):
        super().render(screen)
        self.choice_cards(screen)
        pygame.draw.rect(screen, self.color_name, (self.rect[0], self.rect[1]) + self.rect_name)
        text = self.font.render(name, True, (0, 0, 255))
        screen.blit(text, (self.rect[0] - 15 + self.rect[2] / 2, self.rect[1]))
        if self.clicked == 1:
            self.contour_window(screen)
        if self.now_circle[0] != 0:
            self.contour_circle(self.now_circle[1], screen)
