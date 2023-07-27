import random  # 分别引入要用到的模块
import sys
import pygame


def play(settings):  # 播放器暂停和播放
    if settings.condition == 0:
        settings.condition = 1
        pygame.mixer.music.unpause()  # 播放音乐
    else:
        settings.condition = 0
        pygame.mixer.music.pause()  # 暂停音乐


def change_song(settings, music_list, pos):  # 更换歌曲
    music_list.pos = pos  # 根据参数更改当前播放歌曲坐标
    settings.song_info(music_list)  # 更新当前歌曲信息
    settings.progress = 400  # 调整进度条
    pygame.mixer.music.load('D:/Music_mine/' + music_list.musics[music_list.pos])  # 加载下一首要播放的歌曲
    pygame.mixer.music.play()  # 播放歌曲


def next_song(settings, music_list):  # 切到下一首歌
    if settings.order == 0:  # 播放模式为列表循环
        change_song(settings, music_list, (music_list.pos + 1) % music_list.sum)  # 使用更换歌曲函数，传入参数为该模式下下一首歌在列表中的坐标，下同
    elif settings.order == 1:  # 播放模式为单曲循环
        change_song(settings, music_list, music_list.pos)
    else:  # 播放模式为随机播放
        change_song(settings, music_list, random.choice(range(music_list.sum)))
    settings.condition = 1  # 更换歌曲后自动切换到正在播放状态


def pre_song(settings, music_list):  # 切到上一首歌
    if settings.order == 0:
        change_song(settings, music_list, (music_list.pos + music_list.sum - 1) % music_list.sum)
    elif settings.order == 1:
        change_song(settings, music_list, music_list.pos)
    else:
        change_song(settings, music_list, random.choice(range(music_list.sum)))
    settings.condition = 1


def change_volume_condition(settings):
    settings.volume = -settings.volume  # 更改播放器音量
    if settings.volume < 0:
        pygame.mixer.music.set_volume(0)
    else:
        pygame.mixer.music.set_volume(settings.volume)


def change_volume(settings, pos):
    if pos <= 410:
        settings.volume = 1.0
    elif pos >= 490:
        settings.volume = 0.0
    else:
        settings.volume = (490 - pos) / 80
    pygame.mixer.music.set_volume(settings.volume)


def change_progress(settings, music_list, pos):  # 调整播放进度
    pygame.mixer.music.load('D:/Music_mine/' + music_list.musics[music_list.pos])
    settings.progress = pos  # 调整进度条
    progress = (pos - 400) * music_list.time1[music_list.pos] / 500000
    pygame.mixer.music.play(start=progress, fade_ms=500)  # 从指定进度开始播放
    if settings.condition == 0:
        pygame.mixer.music.pause()


def events_mouse_button_down_check_left(settings, music_list, event):  # 检测鼠标左键按下时箭头坐标，并实现相应功能
    if 520 <= event.pos[0] <= 550 and 510 <= event.pos[1] <= 530:  # 箭头位于切换播放模式图标上
        settings.order = (settings.order + 1) % 3  # 更改播放模式标识
    elif 563 <= event.pos[0] <= 600 and 500 <= event.pos[1] <= 540:  # 箭头位于切到上一首歌图标上
        pre_song(settings, music_list)
    elif 630 <= event.pos[0] <= 670 and 500 <= event.pos[1] <= 540:  # 箭头位于暂停/播放图标上
        play(settings)
    elif 700 <= event.pos[0] <= 737 and 500 <= event.pos[1] <= 540:  # 箭头位于切到下一首歌图标上
        next_song(settings, music_list)
    elif 760 <= event.pos[0] <= 790 and 510 <= event.pos[1] <= 535:  # 更改播放器音量标识
        change_volume_condition(settings)
    elif 760 <= event.pos[0] <= 790 and 405 <= event.pos[1] <= 495:  # 更改播放器音量
        if settings.volume_mouse:
            change_volume(settings, event.pos[1])
    elif 400 <= event.pos[0] <= 900 and 552 <= event.pos[1] <= 568:  # 更改歌曲播放进度
        change_progress(settings, music_list, event.pos[0])
    elif 50 <= event.pos[0] <= 400 and 50 <= event.pos[1] < 500:  # 根据鼠标在列表上的点击切歌
        if (settings.list_start + event.pos[1] - 50) // settings.list_per_height < music_list.sum:
            settings.condition = 1
            change_song(settings, music_list, (settings.list_start + event.pos[1] - 50) // settings.list_per_height)


def events_mouse_motion_check(settings, event):  # 检测鼠标移动
    if 400 <= event.pos[0] <= 900 and 552 <= event.pos[1] <= 568:  # 鼠标悬停在进度条上
        settings.condition_progress = 1
        settings.volume_mouse = 0
        settings.list_mouse = -1
    elif 760 <= event.pos[0] <= 790 and 510 <= event.pos[1] <= 535:  # 鼠标悬停在音量图标上
        settings.condition_progress = 0
        settings.volume_mouse = 1
        settings.list_mouse = -1
    elif 760 <= event.pos[0] <= 790 and 400 <= event.pos[1] <= 510:  # 鼠标悬停在音量条上
        settings.condition_progress = 0
        settings.list_mouse = -1
    elif 50 <= event.pos[0] <= 400 and 50 <= event.pos[1] < 500:  # 鼠标悬停在歌曲列表上
        settings.condition_progress = 0
        settings.volume_mouse = 0
        settings.list_mouse = event.pos[1]
    else:
        settings.condition_progress = 0
        settings.volume_mouse = 0
        settings.list_mouse = -1


def events_mouse_button_down_check_middle(settings, event, sign):  # 检测鼠标滚轮滚动
    if 50 <= event.pos[0] <= 400 and 50 <= event.pos[1] < 500:  # 鼠标悬停在歌曲列表上
        settings.list_move_step += sign * 4 * settings.list_per_height


def events_check(settings, music_list):  # 检测事件发生
    for event in pygame.event.get():  # 在事件队列中监测事件
        if event.type == pygame.QUIT:  # 监测到退出程序请求
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:  # 鼠标移动
            events_mouse_motion_check(settings, event)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 监测到鼠标按下
            if event.button == 1:  # 鼠标按下键为左键
                events_mouse_button_down_check_left(settings, music_list, event)
            elif event.button == 2:  # 鼠标按下键为中间滚轮
                pass
            elif event.button == 3:  # 鼠标按下键为右键
                pass
            elif event.button == 4:  # 鼠标滚轮向前滚动
                events_mouse_button_down_check_middle(settings, event, -1)
            elif event.button == 5:  # 鼠标滚轮向后滚动
                events_mouse_button_down_check_middle(settings, event, 1)


def update_screen(screen, music_list, player_settings):  # 更新屏幕
    screen.fill(player_settings.screen_background)  # 填充颜色
    player_settings.blit_condition(screen, music_list)  # 使用player_settings里面的blit_condition方法更新屏幕内容
    pygame.display.update()  # 刷新屏幕
