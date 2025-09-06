from pygame import *
import sys
PURPLE = (142, 36, 108)
ORANGE = (225, 108, 68)
BLUE = (85, 118, 201)
WHITE = (255, 255, 255)
BUTTONS = ["Start", "Settings", "Exit"]
class Button:
    def __init__(self, text, font, width, height, pos, round_top = False, round_bottom = False):
        self.text = text
        self.font = font
        self.width = width
        self.height = height
        self.pos = pos
        self.round_top = round_top
        self.round_bottom = round_bottom
        self.rect = Rect(pos[0], pos[1], width, height)
    def draw(self, screen, selected = False):
        if self.text == "Start":
            color = ORANGE if selected else PURPLE
        elif self.text == "Settings":
            color = ORANGE if selected else BLUE
        else:
            color = ORANGE if selected else BLUE
        border_radius = 20
        top_left = border_radius if self.round_top else 0
        top_right = border_radius if self.round_top else 0
        bottom_left = border_radius if self.round_bottom else 0
        bottom_right = border_radius if self.round_bottom else 0
        draw.rect(screen, color, self.rect, border_top_left_radius = top_left, border_top_right_radius = top_right, border_bottom_left_radius = bottom_left, border_bottom_right_radius = bottom_right)
        text_surf = self.font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center = self.rect.center)
        screen.blit(text_surf, text_rect)
        