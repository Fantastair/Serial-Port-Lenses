import pygame

color_offset = pygame.Color(20, 20, 20, 0)

BLACK = pygame.Color("#000000")
WHITE = pygame.Color("#ffffff")
FAKEWHITE = pygame.Color("#e3e3e3")
BUTTONBLUE = pygame.Color("#0072c2")


BLACK_6_textstyle = {
    'size': 16,
    'fgcolor': BLACK
}

WHITE_6_textstyle = {
    'size': 16,
    'fgcolor': WHITE
}

NORMAL_buttonstyle = {
    'origin_bg': BUTTONBLUE,
    'origni_sc': None,
    'origin_bd': 0,

    'press_bg': BUTTONBLUE - color_offset,
    'hover_bg': BUTTONBLUE + color_offset,
}

del pygame, color_offset
