import pygame  # 引入模块


class Settings:  # 定义类Settings存储歌曲播放模式、播放状态、图片坐标等信息
    def __init__(self):
        self.screen_width = 1000  # 主窗口宽度
        self.screen_height = 600  # 主窗口高度
        self.screen_background = (233, 233, 233)  # 主窗口背景颜色
        self.list_width = 350  # 歌曲列表宽度
        self.list_height = 450  # 歌曲列表高度
        self.list_background = (235, 235, 235)  # 歌曲列表背景颜色
        self.list_per_height = 30  # 歌曲列表每首歌占格高度
        self.list_start = 0  # 列表展示歌曲开始坐标
        self.list_mouse = -1  # 鼠标是否位于列表位置，-1表示否，否则表示是
        self.list_move_step = 0  # 列表将要滚动的距离，向上滚动为负，向下滚动为正
        self.list_move_speed = 15  # 列表滚动速度
        self.list_backgrounds = [(228, 228, 228), (235, 235, 235)]  # 歌曲列表单双数方格背景颜色
        self.list_backgrounds_mouse_on = (220, 220, 220)  # 鼠标悬停时列表方格背景颜色
        self.list_font = pygame.font.SysFont('SimSun', 13)  # 列表歌曲字体
        self.list_playing0 = pygame.image.load('image/playing0.png')  # 加载列表双数方格正在播放标志
        self.list_playing0 = pygame.transform.scale(self.list_playing0, (20, 20))
        self.rect_list_playing0 = self.list_playing0.get_rect()
        self.rect_list_playing0.x = 60
        self.list_playing1 = pygame.image.load('image/playing1.png')  # 加载列表单数方格正在播放标志
        self.list_playing1 = pygame.transform.scale(self.list_playing1, (20, 20))
        self.rect_list_playing1 = self.list_playing1.get_rect()
        self.rect_list_playing1.x = 60
        self.list_playings = []  # 创建列表存储两个标志，方便下面调用
        self.list_playings.append(self.list_playing0)
        self.list_playings.append(self.list_playing1)
        self.rect_list_playings = []  # 创建列表存储两个标志坐标，方便下面调用
        self.rect_list_playings.append(self.rect_list_playing0)
        self.rect_list_playings.append(self.rect_list_playing1)
        self.list_playing_mouse_on = pygame.image.load('image/playing_mouse_on.png')  # 加载列表鼠标悬停方格正在播放标志
        self.list_playing_mouse_on = pygame.transform.scale(self.list_playing_mouse_on, (20, 20))
        self.rect_list_playing_mouse_on = self.list_playing_mouse_on.get_rect()
        self.rect_list_playing_mouse_on.x = 60
        self.order = 0  # 播放模式标识初始化为0标识列表循环
        self.condition = 1  # 播放状态初始化为1表示正在播放
        self.volume = 0.5  # 播放器音量初始化为1表示不是静音
        self.volume_mouse = 0  # 鼠标图标是否停在音量图标上
        self.volume_background = (245, 245, 245)  # 音量条背景颜色
        self.song_font = pygame.font.SysFont('SimHei', 28)  # 歌曲名字体设置
        self.author_font = pygame.font.SysFont('SimSun', 14)  # 作者名字体设置
        self.pause_button = pygame.image.load('image/pause.bmp')  # 加载暂停按键图标
        self.pause_button = pygame.transform.scale(self.pause_button, (175, 40))
        self.rect_pause = self.pause_button.get_rect()
        self.rect_pause.center = (650, 520)
        self.playing_button = pygame.image.load('image/playing.bmp')  # 加载播放按键图标
        self.playing_button = pygame.transform.scale(self.playing_button, (175, 40))
        self.rect_playing = self.playing_button.get_rect()
        self.rect_playing.center = (650, 520)
        self.order1 = pygame.image.load('image/sequence.bmp')  # 歌曲播放模式图标1
        self.order1 = pygame.transform.scale(self.order1, (35, 29))
        self.rect_order1 = self.order1.get_rect()
        self.rect_order1.center = (535, 520)
        self.order2 = pygame.image.load('image/only_one.bmp')  # 歌曲播放模式图标2
        self.order2 = pygame.transform.scale(self.order2, (35, 29))
        self.rect_order2 = self.order2.get_rect()
        self.rect_order2.center = (535, 520)
        self.order3 = pygame.image.load('image/random.bmp')  # 歌曲播放模式图标3
        self.order3 = pygame.transform.scale(self.order3, (35, 29))
        self.rect_order3 = self.order3.get_rect()
        self.rect_order3.center = (535, 520)
        self.volume_on = pygame.image.load('image/volume_on.png')  # 歌曲音量图标
        self.volume_on = pygame.transform.scale(self.volume_on, (35, 29))
        self.rect_volume_on = self.volume_on.get_rect()
        self.rect_volume_on.center = (775, 520)
        self.volume_off = pygame.image.load('image/volume_off.png')  # 歌曲音量静音图标
        self.volume_off = pygame.transform.scale(self.volume_off, (35, 29))
        self.rect_volume_off = self.volume_off.get_rect()
        self.rect_volume_off.center = (775, 520)
        self.condition_progress = 0  # 歌曲进度条模式标志
        self.progress = 400
        self.progress_background = (203, 203, 203)  # 歌曲进度条底色
        self.progress_color = (255, 0, 0,)  # 歌曲进度条颜色
        self.progress_circle = (215, 0, 0)  # 歌曲进度条圆点颜色
        self.song = None
        self.song_rect = None
        self.author = None
        self.author_rect = None
        self.album = None
        self.album_rect = None

    def song_info(self, music_list):  # 初始化以及切换歌曲时调用
        self.song = self.song_font.render(music_list.albums[music_list.pos][:-4], True, (0, 0, 0),
                                          self.screen_background)  # 更新歌曲名
        self.song_rect = self.song.get_rect()
        self.song_rect.center = (650, 25)
        self.author = self.author_font.render(music_list.musicians[music_list.pos], True, (0, 0, 0),
                                              self.screen_background)  # 更新歌手
        self.author_rect = self.author.get_rect()
        self.author_rect.center = (650, 55)
        self.album = pygame.image.load('album/' + music_list.albums[music_list.pos])  # 更新歌曲专辑图片
        self.album = pygame.transform.scale(self.album, (400, 400))
        self.album_rect = self.album.get_rect()
        self.album_rect.center = (650, 280)

    def blit_order(self, screen, music_list):  # 更新状态栏
        if self.order == 0:  # 更新播放模式图标
            screen.blit(self.order1, self.rect_order1)
        elif self.order == 1:
            screen.blit(self.order2, self.rect_order2)
        else:
            screen.blit(self.order3, self.rect_order3)
        if self.condition:  # 更新播放状态图标
            screen.blit(self.playing_button, self.rect_playing)
        else:
            screen.blit(self.pause_button, self.rect_pause)
        if self.volume > 0:  # 更新音量状态图标
            screen.blit(self.volume_on, self.rect_volume_on)
        else:
            screen.blit(self.volume_off, self.rect_volume_off)
        if self.volume_mouse:  # 更新音量条
            pygame.draw.rect(screen, self.volume_background, (760, 400, 30, 100), border_radius=5)
            pygame.draw.line(screen, self.progress_background, (775, 410), (775, 490), 3)
            if self.volume > 0:
                start = 490 - int(80 * self.volume)
            else:
                start = 490
            pygame.draw.line(screen, self.progress_color, (775, start), (775, 490), 3)
            pygame.draw.circle(screen, self.progress_circle, (775, start), 5)
        pos_now = pygame.mixer.music.get_pos() * 500 // music_list.time[
            music_list.pos] + self.progress  # 歌曲进度
        if self.condition_progress == 0:
            pygame.draw.line(screen, self.progress_background, (400, 560), (900, 560), 3)  # 歌曲进度条底层
            pygame.draw.line(screen, self.progress_color, (400, 560), (pos_now, 560), 3)  # 歌曲进度条进度层
        else:
            pygame.draw.line(screen, self.progress_background, (400, 560), (900, 560), 5)  # 歌曲进度条底层
            pygame.draw.line(screen, self.progress_color, (400, 560), (pos_now, 560), 7)  # 歌曲进度条进度层
            pygame.draw.circle(screen, self.progress_circle, (pos_now, 560), 5)

    def blit_list(self, screen, music_list):  # 更新歌曲列表
        pygame.draw.rect(screen, self.list_background, (50, 50, self.list_width, self.list_height))  # 歌曲列表底层
        num = self.list_height // self.list_per_height  # 歌曲列表中方格数
        if self.list_move_step < 0:  # 列表滚动距离为负，列表应向上滚动
            self.list_move_step += self.list_move_speed
            if self.list_move_step > 0:  # 滚动距离变号的情况
                self.list_move_step = 0
            self.list_start -= self.list_move_speed
            if self.list_start < 0:  # 滚动到列表上端尽头，直接停止滚动，并将要滚动的距离置为0，下面类似
                self.list_start = 0
                self.list_move_step = 0
        elif self.list_move_step > 0:  # 列表滚动距离为正，列表应向下滚动
            self.list_move_step -= self.list_move_speed
            if self.list_move_step < 0:  # 滚动距离变号的情况
                self.list_move_step = 0
            self.list_start += self.list_move_speed
            if self.list_start >= music_list.sum * self.list_per_height - self.list_height:
                self.list_start = music_list.sum * self.list_per_height - self.list_height
                self.list_move_step = 0
        if self.list_height % self.list_per_height == 0:  # 歌曲列表高度能整除每个方格高度情况
            if self.list_start % self.list_per_height:
                num += 1
        else:  # 歌曲列表高度不能整除每个方格高度情况
            num += 1
        start = 50 - self.list_start % self.list_per_height  # 方格初始的y坐标
        song_pos = self.list_start // self.list_per_height  # 当前列表开始歌曲坐标
        for i in range(num):  # 进入循环打印每个方格
            if song_pos >= music_list.sum:
                break
            condition = 0  # 判断方格单双数，初始化为双数
            if song_pos % 2:  # 方格满足单数条件
                condition = 1
            if self.list_mouse < 0:  # 鼠标不悬停在歌曲列表上
                pygame.draw.rect(screen, self.list_backgrounds[condition],
                                 (50, start, self.list_width, self.list_per_height))  # 打印列表中一首歌方格
                song = self.list_font.render(music_list.albums[song_pos][:-4], True, (0, 0, 0),
                                             self.list_backgrounds[condition])  # 更新列表方格当前歌曲名
                if song_pos == music_list.pos:
                    self.rect_list_playings[condition].y = start + (self.list_per_height - 20) / 2  # 赋值给正在播放标志y坐标
                    screen.blit(self.list_playings[condition], self.rect_list_playings[condition])  # 打印正在播放标志
            else:  # 鼠标悬停在歌曲列表上
                if start <= self.list_mouse < start + self.list_per_height:  # 鼠标悬停的方格
                    pygame.draw.rect(screen, self.list_backgrounds_mouse_on,
                                     (50, start, self.list_width, self.list_per_height))  # 打印列表中一首歌方格
                    song = self.list_font.render(music_list.albums[song_pos][:-4], True, (0, 0, 0),
                                                 self.list_backgrounds_mouse_on)  # 更新列表方格当前歌曲名
                    if song_pos == music_list.pos:
                        self.rect_list_playing_mouse_on.y = start + (self.list_per_height - 20) / 2  # 赋值给正在播放标志y坐标
                        screen.blit(self.list_playing_mouse_on, self.rect_list_playing_mouse_on)  # 打印正在播放标志
                else:  # 不是鼠标悬停的方格
                    pygame.draw.rect(screen, self.list_backgrounds[condition],
                                     (50, start, self.list_width, self.list_per_height))  # 打印列表中一首歌方格
                    song = self.list_font.render(music_list.albums[song_pos][:-4], True, (0, 0, 0),
                                                 self.list_backgrounds[condition])  # 更新列表方格当前歌曲名
                    if song_pos == music_list.pos:
                        self.rect_list_playings[condition].y = start + (self.list_per_height - 20) / 2  # 赋值给正在播放标志y坐标
                        screen.blit(self.list_playings[condition], self.rect_list_playings[condition])  # 打印正在播放标志
            song_pos += 1  # 歌曲坐标加一
            song_rect = song.get_rect()  # 得到字体坐标
            song_rect.x = 90  # 赋值给该字体x坐标
            song_rect.y = start + (self.list_per_height - 13) / 2  # 赋值给该字体y坐标
            screen.blit(song, song_rect)  # 打印该方格
            start += self.list_per_height  # 更新方格初始y坐标
        pygame.draw.rect(screen, self.screen_background, (50, 0, self.list_width, 50))  # 掩盖超出列表框上端的字体
        pygame.draw.rect(screen, self.screen_background, (50, 500, self.list_width, 100))  # 掩盖超出列表框下端的字体

    def blit_song(self, screen):  # 更新歌曲信息
        screen.blit(self.song, self.song_rect)
        screen.blit(self.author, self.author_rect)
        screen.blit(self.album, self.album_rect)

    def blit_condition(self, screen, music_list):  # 更新屏幕上的显示的专辑图片、歌曲名等信息
        self.blit_song(screen)  # 更新歌曲信息
        self.blit_list(screen, music_list)  # 更新歌曲列表
        self.blit_order(screen, music_list)  # 更新状态栏
