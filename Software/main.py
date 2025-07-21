DEBUG = True

import pygame
from pathlib import Path
if DEBUG:
    import os
    cwd = Path(os.getcwd())
    os.chdir(cwd / "Software")

import fantas
from fantas import uimanager as u

u.settings = fantas.load(Path(".settings"))

u.init((0, 0) if u.settings["window_maxsize"] else u.settings['window_size'], 1, pygame.SRCALPHA | pygame.RESIZABLE)
pygame.display.set_caption(u.settings['window_title'])
pygame.event.set_blocked([pygame.ACTIVEEVENT, pygame.VIDEORESIZE, pygame.VIDEOEXPOSE])

u.images = fantas.load_res_group(Path("Display/assets/image").iterdir())
u.fonts = fantas.load_res_group(Path("Display/assets/font").iterdir())
pygame.display.set_icon(u.images['icon2'])

from Display import root
u.root = root.root
root.root.init()

def quit():
    fantas.dump(u.settings, Path(".settings"))
    pygame.quit()
    import sys
    sys.exit(0)

u.mainloop(quit)
