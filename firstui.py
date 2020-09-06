import tkinter as tk
import tkinter.colorchooser
import pygame as py
import time
import _thread
from tkinter import *
import cv2
from PIL import Image, ImageTk
import multiprocessing
import math
from videopage import videopage #视频播放界面
from photopage import photopage #相册界面
from musicpage import musicpage #音乐界面
winwidth = 0
winheight = 0


#桌面
class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry(str(winwidth)+'x'+str(winheight))
        
        initface(self.root)

#初始界面
class initface():
    def __init__(self,master):
        self.master = master
        #基准界面initface
        self.initface = tk.Canvas(self.master,bg="white",width=winwidth,height=winheight)
        self.initface.pack()
        self.initface.configure(highlightthickness=0)
        #常量定义
        self.Bigbtnwidth=winwidth/3 #中央大按钮的大小
        self.btnwidth=winheight/4 #普通按钮的大小
        self.padding1=40 #普通按钮之间的间隔
        self.midlength = winwidth*9/24
        self.sidelength = winwidth*15/48
        self.tomid = 50 
        self.Amovex = winwidth/3-self.padding1-self.btnwidth-self.tomid
        self.Bmovey = winheight/4
        self.Cmovex = winwidth*2/3+self.padding1+self.tomid
        self.midmove = 60 #中间层按钮偏移量
        #偏移量
        self.move = [
                     [self.Amovex,self.Bmovey-self.btnwidth/2-self.padding1/2],[self.Amovex-self.midmove,self.Bmovey+self.btnwidth/2+self.padding1/2],[self.Amovex,self.Bmovey+self.btnwidth*3/2+self.padding1*3/2],
                     [winwidth/3,0],[winwidth/3,self.Bmovey],[self.sidelength,winheight*5/6],
                     [self.Cmovex,self.Bmovey-self.btnwidth/2-self.padding1/2],[self.Cmovex+self.midmove,self.Bmovey+self.btnwidth/2+self.padding1/2],[self.Cmovex,self.Bmovey+self.btnwidth*3/2+self.padding1*3/2]
                    ]
        #读取图片
        self.titleimage = ImageTk.PhotoImage(Image.open("srcimage/title.jpg").resize((int(winwidth/3),int(winheight/6))))  
        self.backgroundimage = ImageTk.PhotoImage(Image.open("srcimage/test.jpg").resize((int(winwidth),int(winheight))))  
        self.bookimage = ImageTk.PhotoImage(Image.open("srcimage/book.jpg").resize((int(self.btnwidth),int(self.btnwidth))))
        self.movieimage = ImageTk.PhotoImage(Image.open("srcimage/movie.jpg").resize((int(self.btnwidth),int(self.btnwidth))))
        self.musicimage = ImageTk.PhotoImage(Image.open("srcimage/music.jpg").resize((int(self.btnwidth),int(self.btnwidth))))
        self.studyimage = ImageTk.PhotoImage(Image.open("srcimage/study.jpg").resize((int(self.btnwidth),int(self.btnwidth))))
        self.gameimage = ImageTk.PhotoImage(Image.open("srcimage/game.jpg").resize((int(self.btnwidth),int(self.btnwidth))))
        self.workimage = ImageTk.PhotoImage(Image.open("srcimage/work.gif").resize((int(self.Bigbtnwidth),int(self.Bigbtnwidth))))
        # 右边的三个按钮
        self.buttonA_1 = tk.Button(self.initface,image=self.bookimage,height=self.btnwidth,width=self.btnwidth,relief="ridge",command=self.gotophoto)
        self.buttonA_1.place(x=self.move[0][0],y=self.move[0][1])
        self.buttonA_2 = tk.Button(self.initface,image=self.movieimage,height=self.btnwidth,width=self.btnwidth,relief="ridge",command=self.gotovideo)
        self.buttonA_2.place(x=self.move[1][0],y=self.move[1][1])
        self.buttonA_3 = tk.Button(self.initface,image=self.musicimage,height=self.btnwidth,width=self.btnwidth,relief="ridge",command=self.gotomusic)
        self.buttonA_3.place(x=self.move[2][0],y=self.move[2][1])
        # 交大的校徽
        self.titleCanvas = tk.Canvas(self.initface,width=self.Bigbtnwidth,height=winheight/6)
        self.titleCanvas.place(x=self.move[3][0],y=self.move[3][1])
        self.titleCanvas.create_image(0,0,anchor='nw',image=self.titleimage)  
        self.titleCanvas.configure(highlightthickness=0)
        # 中间的按钮
        self.buttonB = tk.Button(self.initface,image=self.workimage,height=int(winheight/2),width=int(winwidth/3),relief="ridge")
        self.buttonB.place(x=self.move[4][0],y=self.move[4][1])
        # 左边的三个按钮
        self.buttonC_1 = tk.Button(self.initface,image=self.studyimage,height=self.btnwidth,width=self.btnwidth,relief="ridge")
        self.buttonC_1.place(x=self.move[6][0],y=self.move[6][1])
        self.buttonC_2 = tk.Button(self.initface,image=self.gameimage,height=self.btnwidth,width=self.btnwidth,relief="ridge")
        self.buttonC_2.place(x=self.move[7][0],y=self.move[7][1])
        self.buttonC_3 = tk.Button(self.initface,image=self.bookimage,height=self.btnwidth,width=self.btnwidth,relief="ridge")
        self.buttonC_3.place(x=self.move[8][0],y=self.move[8][1])

        #刷新显示图片
        self.showtitle()

    def gotovideo(self):       
        #self.initface.destroy()
        videopage(self.master,winheight,winwidth)
    def gotophoto(self):
        #self.initface.destroy()
        photopage(self.master,winheight,winwidth)
    def gotomusic(self):
        musicpage(self.master,winheight,winwidth)
    #播放音乐
    def play_music(threadName, delay):
            filepath = r"D:\music\test.mp3"
            py.mixer.init()
            # 加载音乐
            py.mixer.music.load(filepath)
            py.mixer.music.play(start=0.0)
            #播放时长，没有此设置，音乐不会播放，会一次性加载完
            time.sleep(300)
            py.mixer.music.stop()
    def xz():
        color=tkinter.colorchooser.askcolor()
        colorstr=str(color)
        print('打印字符串%s 切掉后=%s' % (colorstr,colorstr[-9:-2]))
        lb.config(text=colorstr[-9:-2],background=colorstr[-9:-2])

    #拨打电话
    def callfamily():
        print("拨打中")

    #测量血压
    def bloodpressure():
        print("测量中")

    #听音乐
    def listenmusic():
        print("听音乐")
        _thread.start_new_thread( play_music, ("Thread-1", 2, ))
    #紧急呼救
    def emecall(self,event):
        x = event.x
        y = event.y
        if self.isincircle(x,y,winwidth/2,winheight/2,(self.midlength-120)/2):
            self.gotovideo()
        print(event)
    def showtitle(self,):
        def video_loop():
            try:
                while True:
                    self.initface.create_image(0,0,anchor='nw',image=self.backgroundimage)
                    self.titleCanvas.create_image(0,0,anchor='nw',image=self.titleimage)  
                   
                    self.master.update_idletasks()  #最重要的更新是靠这两句来实现
                    self.master.update()
            except:
                pass
            
        video_loop()
        #self.face1.mainloop()
    #计算两点的距离
    def distance(self,x1,y1,x2,y2):
        return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
    #判断某个点是否在圆的范围内
    def isincircle(self,x,y,x0,y0,radius):
        return self.distance(x,y,x0,y0)<radius

if __name__ == '__main__':    
    root = tk.Tk()
    #全屏应用
    root.attributes("-fullscreen",True)
    #获取宽高
    winwidth = root.winfo_screenwidth()
    winheight = root.winfo_screenheight()
    basedesk(root)
    root.mainloop()


# root = tk.Tk()

# img_png = tkinter.PhotoImage(file = 'banana.gif')
# label_img = tkinter.Label(root, image = img_png)
# label_img.pack()
# root.mainloop()