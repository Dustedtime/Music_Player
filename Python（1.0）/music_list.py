class MusicList:  # 定义类MusicList存储歌曲、作者等信息
    def __init__(self):
        self.musicians = ['羽肿', 'Athletics', '冰幽，解忧草', '四季音色', 'ycccc', '奇然，沈谧仁', 'Aki阿杰，银临',
                          'Candy_Wind', '王梓钰', '霍尊', '任然', '羽肿', '羽肿', 'Aya岚', 'Funton', 'GALA',
                          'Hea2t', 'Jannik', 'Uri,喵☆酱', '阿YueYue', '阿冗', '艾辰', '陈奕迅', '华晨宇',
                          '华晨宇,杨宗纬', '金贵晟', '李常超（Lao乾妈）', '任然', '盛哲', '司南', '四季音色', '太一',
                          '王菲', '小时姑娘', '小星星Aurora', '心然', '杨博然', '音阙诗听', '音阙诗听,王梓钰',
                          '音阙诗听,王梓钰', '银临', '银临', '御鹿神谷,漆柚', '云朵', '周笔畅', '周杰伦',
                          '周杰伦', '周杰伦', '周深', '嗨的HiDii国乐团,河伯', '福禄寿FloruitShow', '西瓜JUN']  # 作者列表
        self.musics = ['羽肿 - Windy Hill.mp3', 'Athletics - III.mp3', '冰幽,解忧草 - 辞·九门回忆.mp3',
                       '四季音色 - 归途.mp3',
                       'ycccc - 满天星辰不及你(3).mp3', '奇然,沈谧仁 - 琵琶行.mp3', 'Aki阿杰,银临 - 牵丝戏.mp3',
                       'Candy_Wind - 青空.mp3', '音阙诗听,王梓钰 - 人间芳菲.mp3', '霍尊 - 天行九歌.mp3',
                       '任然 - 外婆桥.mp3',
                       '羽肿 - 夏に花が散る.mp3', '羽肿 - 花火が瞬く夜に.mp3', 'Aya岚 - 有你的江湖.mp3', 'Funton - 别念.mp3',
                       'GALA - 追梦赤子心.mp3', 'Hea2t - 初夏的风.mp3', 'Jannik - Grace.mp3', 'Uri,喵☆酱 - 鸳鸯债.mp3',
                       '阿YueYue - 予君书.mp3', '阿冗 - 你的答案.mp3', '艾辰 - 错位时空.mp3', '陈奕迅 - 孤勇者.mp3',
                       '华晨宇 - 烟火里的尘埃.mp3', '华晨宇,杨宗纬 - 国王与乞丐.mp3', '金贵晟 - 虹之间.mp3',
                       '李常超（Lao乾妈） - 盗墓笔记·十年人间.mp3', '任然 - 山外小楼夜听雨.mp3', '盛哲 - 在你的身边.mp3',
                       '司南 - 冬眠.mp3', '四季音色 - 曙光.mp3', '太一 - 负重一万斤长大.mp3', '王菲 - 如愿.mp3',
                       '小时姑娘 - 爱殇 (电视剧《东宫》片头曲).mp3', '小星星Aurora - 坠落星空.mp3',
                       '心然 - 仙剑奇侠传四-织梦行云·离歌.mp3', '杨博然 - 拂袖.mp3', '音阙诗听 - 红昭愿.mp3',
                       '音阙诗听,王梓钰 - 大雪.mp3', '音阙诗听,王梓钰 - 小满.mp3', '银临 - 流光记.mp3',
                       '银临 - 棠梨煎雪.mp3', '御鹿神谷,漆柚 - 功成名就.mp3', '云朵 - 我的楼兰.mp3',
                       '周笔畅 - 最美的期待.mp3', '周杰伦 - 青花瓷.mp3', '周杰伦 - 晴天.mp3', '周杰伦 - 夜曲.mp3',
                       '周深 - 请笃信一个梦.mp3', '嗨的HiDii国乐团,河伯 - 【洞箫】天行九歌（Cover 霍尊）.mp3',
                       '福禄寿FloruitShow - 我用什么把你留住 (Remix).mp3', '西瓜JUN - 寄妻书.mp3']
        self.albums = ['Windy Hill.jpg', 'III.jpg', '辞·九门回忆.jpg', '归途.jpg', '满天星辰不及你.jpg', '琵琶行.jpg',
                       '牵丝戏.jpg', '青空.jpg',
                       '人间芳菲.jpg', '天行九歌.jpg', '外婆桥.jpg', '夏天花谢了.jpg', '烟花绽放的夜晚.jpg',
                       '有你的江湖.jpg', '别念.jpg', '追梦赤子心.jpg', '初夏的风.jpg', 'Grace.jpg', '鸳鸯债.jpg',
                       '予君书.jpg', '你的答案.jpg', '错位时空.jpg', '孤勇者.jpg', '烟火里的尘埃.jpg',
                       '国王与乞丐.jpg', '虹之间.jpg', '十年人间.jpg', '山外小楼夜听雨.jpg', '在你的身边.jpg',
                       '冬眠.jpg', '曙光.jpg', '负重一万斤长大.jpg', '如愿.jpg', '爱觞.jpg', '坠落星空.jpg',
                       '织梦行云·离歌.jpg', '拂袖.jpg', '红昭愿.jpg', '大雪.jpg', '小满.jpg', '流光记.jpg',
                       '棠梨煎雪.jpg', '功成名就.jpg', '我的楼兰.jpg', '最美的期待.jpg', '青花瓷.jpg',
                       '晴天.jpg', '夜曲.jpg', '请笃信一个梦.jpg', '天行九歌-洞箫.jpg',
                       '我用什么把你留住.jpg', '寄妻书.jpg']  # 专辑图片名列表
        self.time = [308000, 370000, 241000, 174000, 216000, 335000, 239000, 201000, 208000, 234000, 261000, 283000,
                     270000, 90000, 234000, 317000, 209000, 300000, 147000, 203000, 219000, 204000, 256000, 321000,
                     245000, 246000, 277000, 249000, 262000, 269000, 110000, 262000, 265000, 304000, 236000, 139000,
                     247000, 173000, 200000, 206000, 285000, 245000, 241000, 329000, 210000, 239000, 269000, 226000,
                     261000, 234000, 325000, 229000]  # 文件属性显示的歌曲时长/毫秒
        self.time1 = [308000, 370000, 241000, 174000, 216000, 335000, 239000, 201000, 208000, 234000, 261000, 283000,
                      270000, 90000, 234000, 317000, 209000, 300000, 160000, 221000, 239000, 222000, 256000, 321000,
                      245000, 246000, 277000, 249000, 285000, 269000, 110000, 262000, 265000, 304000, 236000, 139000,
                      247000, 188000, 200000, 206000, 285000, 245000, 241000, 329000, 210000, 239000, 269000, 226000,
                      285000, 234000, 325000, 229000]  # 歌曲真实时长/毫秒
        self.pos = 0  # 当前播放歌曲在列表中的位置，初始化为0
        self.sum = 52  # 当前列表中歌曲数目
