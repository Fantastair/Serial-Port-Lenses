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

print("Settings loaded:", u.settings)

u.init(u.settings['window_size'], 1, pygame.SRCALPHA | pygame.RESIZABLE)
pygame.display.set_caption(u.settings['window_title'])

u.root = fantas.Root(pygame.Color('black'))

def quit():
    fantas.dump(u.settings, Path(".settings"))
    pygame.quit()
    import sys
    sys.exit(0)

u.mainloop(quit)
