from pathlib import Path
import pygame
import fantas
from fantas import uimanager as u

settings_path = Path(".settings")

def load_settings():
    """
    加载配置文件，如果不存在，则生成默认内容的配置文件
    """
    if settings_path.exists():
        u.settings = fantas.load(settings_path)
    else:
        u.settings = {
            "window.title": "串口透镜",      # 窗口标题
            "window.size": (1024, 576),      # 窗口实际大小
            "window.minsize": (480, 720),    # 窗口最小大小
            "window.maximize": True          # 窗口最大化
        }

def save_settings():
    """
    保存当前设置到配置文件
    """
    fantas.dump(u.settings, settings_path)

def auto_set_window_size():
    """
    自动设置窗口大小
    """
    if u.settings["window.maximize"]:
        fantas.maximize_window()
    # else:
        
