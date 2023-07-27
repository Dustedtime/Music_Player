import pygame  # 引进模块
from settings import Settings  # 从其他模块引进要用到的类以及函数
from music_list import MusicList
import music_player_functions as mpf


def run_player():  # 主函数
    pygame.init()  # 初始化程序
    player_settings = Settings()  # 实例化Settings
    player_list = MusicList()  # 实例化MusicList
    screen = pygame.display.set_mode((player_settings.screen_width, player_settings.screen_height))  # 创建主窗口
    pygame.display.set_caption("音乐播放器")  # 设置窗口标题
    player_settings.song_info(player_list)  # 初始化歌曲信息
    pygame.mixer.music.load('D:/Music_mine/' + player_list.musics[player_list.pos])  # 开始运行时先加载第一首歌曲并播放
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(player_settings.volume)
    clock = pygame.time.Clock()  # 设置clock控制循环频率
    while True:  # 主循环
        clock.tick(60)  # 每秒循环60次
        mpf.events_check(player_settings, player_list)  # 检查事件的发生
        mpf.update_screen(screen, player_list, player_settings)  # 更新屏幕
        if not pygame.mixer.music.get_busy() and player_settings.condition:  # 播放结束时自动切到下一首歌
            mpf.next_song(player_settings, player_list)


run_player()
