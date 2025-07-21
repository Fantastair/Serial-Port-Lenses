import pygame
import fantas
from fantas import uimanager as u
from Display.style import *

class IndexPage(fantas.Label):
    BG = WHITE
    
    def __init__(self, size, **anchor):
        super().__init__(size, 0, IndexPage.BG, None, **anchor)
