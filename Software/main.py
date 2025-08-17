DEBUG = True

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''

import pygame
from pathlib import Path
if DEBUG:
    cwd = Path(os.getcwd())
    os.chdir(cwd / "Software")

import fantas
from fantas import uimanager as u

import settings

settings.load_settings()
if DEBUG:
    print("Settings: {")
    for key, value in u.settings.items():
        print(f"  {key}: {value}")
    print("}")

u.init(u.settings['window.size'], pygame.SRCALPHA | pygame.RESIZABLE)
settings.auto_set_window_size()
pygame.display.set_caption(u.settings['window.title'])
pygame.event.set_blocked([pygame.ACTIVEEVENT, pygame.VIDEORESIZE, pygame.VIDEOEXPOSE])
u.images = fantas.load_res_group(Path("Display/assets/image").iterdir())
u.fonts = fantas.load_res_group(Path("Display/assets/font").iterdir())
pygame.display.set_icon(u.images['icon2'])

from Display import root
u.root = root.root
root.root.init()

def quit():
    pygame.quit()
    import sys
    sys.exit(0)

try:
    u.mainloop(quit)
finally:
    quit()
