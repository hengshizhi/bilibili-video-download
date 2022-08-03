#这是我基于下面的一个项目写得一个CMD操控工具
它可以用来操控cmd来下载视频，很原始的方法，所以下载视频的时候不要动
    需要的依赖项
    pyautogui
    要环境变量里有aria2c和ffmpeg
    使用了另一个项目：bilibili_own_tools
    需要安装在cmd可以触及的地方

#一下是bilibili_own_tools原文
bilibili_own_tools
It is a learning project<br>
自编小程序<br>
## downloader.py
    为下载脚本，输入BV号，P数，选择画质
    调用powershell使用aria2c下载，并用ffmpeg合并 
    要环境变量里有aria2c和ffmpeg
## playnum.py
    为实时UP主播放数获取
## getaid.py
    bv转av，获取稿件信息
## downloader_new.py
    更新的下载脚本，待完善
    计划支持稿件信息获取，多种封装下载
迁移至[bilibili-downloader-py](https://github.com/Daniel2022/bilibili-downloader-py)
## coin.py
    投硬币脚本
    随机向5个稿件投5个硬币
    （懒人升级用）# Ten-weaving-s-bilibili-video-download
