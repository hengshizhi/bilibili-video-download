from time import sleep
import pyautogui
import sys

#bilibili星姮十织

def jr_cmd (data):  #把命令键入cmd并运行
    for ll in range(len(data)):
        pyautogui.press(data[ll])
    pyautogui.press('enter')


def cmd (): #打开cmd
    pyautogui.keyDown('win')
    pyautogui.keyDown('r')
    pyautogui.keyUp('win')
    pyautogui.keyUp('r')
    pyautogui.typewrite('cmd')
    pyautogui.press('enter')



sui = '【A】下载视频\n【B】设置\n【C】软件信息\n【D】注意事项\n请输入：'

ssui = input(sui)

if (ssui == 'A'):
    hzUI = (
    '画质选择:\n'
    '4K:120(大会员);\n'
    '1080p60: 116(大会员);\n'
    '720p60: 74;\n'
    '1080p: 80;\n'
    '720p: 64;\n'
    '480p: 32;\n'
    '360p: 16;\n'
    )
    Pv_s = 0
    pv = 1
    bv = input('请输入视频bv号：')
    psss = input('【A】下载指定P，【B】指定下载到多少P,【C】视频没有P：')
    if(psss == 'A'):
        pv = input('下载哪一P：')
        Pv_s = 1
    elif(psss == 'C'):
        p = 0
    else:
        p = input('下载到多少P：')
    #mls = sys.argv[0]#input('请输入视频下载器的路径：')
    ml  = 'c:/bi/'#print('下载路径:',mls.replace('p2p.py', ''))#确认下载路径
    mling = 'python d.py'
    hz = input(hzUI)
    shijian = input('每次下载结束等待时间(整数)：')
    cmd()

    pyautogui.press('c')
    pyautogui.press('d')
    pyautogui.press('space')
    jr_cmd(ml)
    if (int(p) >= 1):
        ppp = 1
        for pp in range(int(p)):
            jr_cmd(mling)
            jr_cmd(bv)
            jr_cmd(str(ppp))
            jr_cmd(hz)
            if (hz == '80'):
                HEVC = Y 
            jr_cmd(Y)
            ppp += 1
            pyautogui.press('enter')
            sleep(int(shijian))
    elif(Pv_s == 1):
        jr_cmd(mling)
        jr_cmd(bv)
        jr_cmd(str(pv))
        jr_cmd(hz)
        if (hz == '80'):
            HEVC = Y 
        jr_cmd(Y)
        pyautogui.press('enter')
        sleep(int(shijian))
    else:
        jr_cmd(mling)
        jr_cmd(bv)
        jr_cmd(hz)
        if (hz == '80'):
            HEVC = Y 
        jr_cmd(Y)
    sleep(int(shijian))
    gb = 'exit'
    jr_cmd(gb)
elif(ssui == 'B'):
    print ('<【A】返回首页\n')
    print('设置未开放\n')
    sz = input('请输入:')
    if (sz == 'A'):
        cmd()
        gzml = sys.argv[0]
        print (gzml)
        jr_cmd('cd '+gzml) 
elif(ssui == 'C'):
    print('软件作者：星姮十织\n代码仓库:https://github.com/hengshizhi/bilibili-video-download\n使用其他项目：bilibili_own_tools')
elif(ssui == 'D')
    print('注意实现：\n 1>视频下载时最好不要动，除非下载较大视频在走进度条 \n 2>本cmd操控器还有很多的bug，我会继续更新，敬请期待')

#pyautogui.typewrite('cd',' ',ml)

#pyautogui.typewrite('cd C:/cd C:/')
