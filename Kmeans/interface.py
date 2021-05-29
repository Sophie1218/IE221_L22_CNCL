from pygame.font import Font
from pygame import Rect
from pygame.display import set_mode as s
from pygame.draw import rect
from pygame import Color
from pygame.display import set_mode, set_caption

validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
# color variables
BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PINK = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRASS = (55, 155, 65)
GREY = (38, 50, 56)

LIGHT_RED = (255, 230, 230)
LIGHT_GREEN = (233, 255, 230)
LIGHT_BLUE = (230, 230, 255)
LIGHT_YELLOW = (255, 253, 235)
LIGHT_PINK = (255, 250, 250)
LIGHT_SKY = (230, 255, 255)
LIGHT_ORANGE = (255, 242, 235)
LIGHT_GRASS = (240, 244, 195)
LIGHT_GREY = (236, 239, 241)

COLORS = [RED, GREEN, BLUE, YELLOW, PINK, SKY, ORANGE, GRASS, GREY]
LIGHT_COLORS = [LIGHT_RED, LIGHT_GREEN, LIGHT_BLUE, LIGHT_YELLOW, LIGHT_PINK, LIGHT_SKY, LIGHT_ORANGE, LIGHT_GREY,
                LIGHT_GRASS]


class TextBox:
    def __init__(self, content, coordinates, color_text, color_rect):
        self.content = content
        self.font_text = None
        self.font_size = 40
        self.color_text = color_text
        font = Font(self.font_text, self.font_size)
        self.text = font.render(self.content, True, self.color_text)
        self.coordinates = coordinates
        self.color_rect = color_rect
        self.rect = Rect(self.coordinates[0], self.coordinates[1], self.text.get_width() + 10,
                         self.text.get_height() + 5)

    def update_text(self, content):
        self.content = content
        self.text = Font(self.font_text, self.font_size).render(self.content, True, self.color_text)

    def update_width_rect(self, size):
        self.rect = Rect(self.coordinates[0], self.coordinates[1], size, self.text.get_height() + 5)

    def update_font_text(self, font):
        self.font_text = font
        font = Font(self.font_text, self.font_size)
        self.text = font.render(self.content, True, self.color_text)

    def update_font_size(self, size):
        self.font_size = size
        font = Font(self.font_text, self.font_size)
        self.text = font.render(self.content, True, self.color_text)

    def update_coordinates(self, coordinates):
        self.coordinates = coordinates
        self.rect = Rect(self.coordinates[0], self.coordinates[1], self.text.get_width() + 10,
                         self.text.get_height() + 5)

    def update_color_text(self, color_text):
        self.color_text = color_text
        font = Font(self.font_text, self.font_size)
        self.text = font.render(self.content, True, self.color_text)

    def update_color_rect(self, color_rect):
        self.color_rect = color_rect

    def delete(self):
        self.content = None
        self.text = None
        self.font_text = None
        self.font_size = None
        self.coordinates = None
        self.color_text = None
        self.color_rect = None
        self.rect = None

    def show(self, screen):
        rect(screen, self.color_rect, self.rect)
        screen.blit(self.text, (self.rect.x + 5, self.rect.y + 5))

    def is_click(self, event):
        if self.rect.collidepoint(event):
            return True

    def get_text_width(self):
        return self.text.get_width()

    def return_content(self):
        return self.content

    def return_content(self):
        return self.content


class InputTextBox(TextBox):
    active = False
    color_active = Color('lightskyblue3')

    def __init(self, *args, **kwargs):

        super.__init__(self, *args, **kwargs)

    def is_click(self, event):
        if self.rect.collidepoint(event):
            return True

    def update_active(self, temp):
        self.active = temp

    def is_active(self):
        return self.active

    def minus_chr(self):
        self.content = self.content[:-1]
        self.update_text(self.content)

    def add_chr(self, char, shiftDown):
        if char in validChars and not shiftDown:
            self.content += char
        elif char in validChars and shiftDown:
            self.content += shiftChars[validChars.index(char)]
        self.update_text(self.content)

    def show(self, screen):
        if self.active:
            rect(screen, self.color_active, self.rect, 2)
        else:
            rect(screen, self.color_rect, self.rect, 2)
        screen.blit(self.text, (self.rect.x + 5, self.rect.y + 5))


def screen(x=1200, y=700):
    return set_mode((x, y))


def caption(name='K - means Visualization'):
    set_caption(name)

# # Demo
# pygame.init()
# shiftDown = False
# screen = screen()
#
# caption()
#
# running = True
#
# clock = pygame.time.Clock()
#
# BACKGROUND = (214, 214, 214)
#
# demo = InputTextBox('', (50, 50), BLACK, BLACK)
# demo.update_width_rect(300)
# while running:
#     clock.tick(60)
#     screen.fill(BACKGROUND)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if demo.is_click(event.pos):
#                 demo.update_active(True)
#             else:
#                 demo.update_active(False)
#         if event.type == pygame.KEYUP:
#             if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
#                 shiftDown = False
#         if event.type == pygame.KEYDOWN:
#             if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
#                 shiftDown = True
#             if demo.is_active():
#                 if event.key == pygame.K_BACKSPACE:
#                     demo.minus_chr()
#                 else:
#                     demo.add_chr(pygame.key.name(event.key))
#                 demo.update_width_rect(max(300, demo.get_text_width() + 10))
#                 print(demo.content)
#     demo.show(screen)
#
#     pygame.display.flip()
#
# pygame.quit()
