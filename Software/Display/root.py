import pygame
import fantas
from fantas import uimanager as u
from Display.style import *
import Display.index as index

class MainRoot(fantas.Root):
    BG = FAKEWHITE
    WIDTH_SPLIT = 640    # 切换显示模式的宽度分界线
    INDEX_NORMAL_WIDTH = 320    # 正常模式下的索引页宽度

    def __init__(self):
        super().__init__(MainRoot.BG)
        self.icon = fantas.Ui(u.images['icon1'], center=(u.WIDTH/2, u.HEIGHT/2))
        self.icon.size = (min(u.WIDTH, u.HEIGHT, 1024 / 0.8) * 0.8, min(u.WIDTH, u.HEIGHT, 1024 / 0.8) * 0.8)
        self.icon.join(self)
        self.icon_pos_kf = fantas.RectKeyFrame(self.icon, 'center', (40, 40), 30, fantas.radius_curve)
        self.icon_size_kf = fantas.UiKeyFrame(self.icon, 'size', (64, 64), 30, fantas.radius_curve)
        self.state = None
        self.index_page = index.IndexPage((0, 0), topleft=(0, 0))
        self.index_page.anchor = 'topleft'

    def init(self):
        t1 = fantas.Trigger()
        t2 = fantas.Trigger()
        t1.bind_endupwith(self.icon_size_kf.launch, 'continue')
        t2.bind_endupwith(self.icon_pos_kf.launch, 'continue')
        t1.launch(30)
        t2.launch(30)
        if u.WIDTH < u.settings['window_minsize'][0] or u.HEIGHT < u.settings['window_minsize'][1]:
            self.state = "too small"
            self.icon_size_kf.curve = self.icon_pos_kf.curve = fantas.harmonic_curve
            self.icon_size_kf.totalframe = self.icon_pos_kf.totalframe = 15
            self.icon_size_kf.value = (self.icon.size[0] - 48, self.icon.size[1] - 48)
            self.icon_pos_kf.value = (self.icon.rect.center[0], self.icon.rect.center[1] - 48)

            tip_text = fantas.Text("窗口尺寸过小，不能正常显示内容！", u.fonts['deyi'], BLACK_6_textstyle, midbottom=(self.icon.rect.centerx, u.HEIGHT/2+self.icon_size_kf.value[1]/2.5))
            tip_text.join(self)
            tip_text.alpha = 0
            tip_text_alpha_kf = fantas.UiKeyFrame(tip_text, 'alpha', 255, 15, fantas.curve)
            t3 = fantas.Trigger()
            t3.bind_endupwith(tip_text_alpha_kf.launch, 'continue')
            t3.launch(30)

            quit_button = fantas.SmoothColorButton((120, 32), NORMAL_buttonstyle, 0, radius={'border_radius': 8}, midtop=(tip_text.rect.centerx, tip_text.rect.bottom + 24))
            quit_button.alpha = 0
            quit_button.join(self)
            quit_button.bind(pygame.event.post, pygame.event.Event(pygame.QUIT))
            fantas.Text("确定", u.fonts['deyi'], WHITE_6_textstyle, center=(quit_button.rect.w/2, quit_button.rect.h/2)).join(quit_button)
            quit_button_alpha_kf = fantas.UiKeyFrame(quit_button, 'alpha', 255, 15, fantas.curve)
            t4 = fantas.Trigger()
            t4.bind_endupwith(quit_button_alpha_kf.launch, 'continue')
            t4.launch(30)
        else:
            if u.WIDTH < 640:
                self.state = "small"
                self.index_page.set_size((u.WIDTH, u.HEIGHT))
            else:
                self.state = "normal"
                self.index_page.set_size((MainRoot.INDEX_NORMAL_WIDTH, u.HEIGHT))
            self.index_page.join_to(self, 0)

root = MainRoot()
