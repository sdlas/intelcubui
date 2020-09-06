import tkinter as tk
import tkinter.colorchooser
import pygame as py
import time
import _thread
from tkinter import *
import cv2
from PIL import Image, ImageTk
import multiprocessing
winheight = 0
winwidth = 0
musiclist = ["music1.jpg","music2.jpg","music3.jpg","music4.jpg","music5.jpg"]
class musicpage():
    def __init__(self,master,_winheight,_winwidth):
        
        self.winheight = _winheight
        self.winwidth = _winwidth
        self.photopadding = self.winwidth/128
        self.photoleftpadding = 500
        self.photowidth = self.winwidth-self.photopadding*2-self.photoleftpadding
        self.photoheight = 70
        self.photomovex = (self.winwidth-self.photowidth)/2
        self.master = master
        self.musicreadlist=[]
        self.topheight = 130 #顶部标题高度
        self.backbtnheight = self.topheight/2
        self.backbtnwidth = self.backbtnheight
        self.backbtnpadding = self.topheight/4 #顶部按钮的间距
        self.pausebtnwidth =40
        self.pausebtnmovey = (self.photoheight-self.pausebtnwidth)/2
        self.pausebtnmovex = self.photowidth-30-self.pausebtnwidth
        self.curid = -1
        #读取图片
        self.backimg = ImageTk.PhotoImage(Image.open("srcimage/toleft.jpg").resize((int(self.backbtnwidth),int(self.backbtnheight)))) 
        self.pauseimg = ImageTk.PhotoImage(Image.open("srcimage/pause.jpg").resize((int(self.pausebtnwidth),int(self.pausebtnwidth)))) 
        self.playimg = ImageTk.PhotoImage(Image.open("srcimage/play.jpg").resize((int(self.pausebtnwidth),int(self.pausebtnwidth)))) 
        self.musicpage=tk.Frame(self.master,width=self.winwidth,height=self.winheight)
        self.musicpage.place(x=0,y=0)
        self.photocanvas = tk.Canvas(self.musicpage,bg="pink",width=self.winwidth,height=self.winheight)
        self.photocanvas.place(x=0,y=0)
        self.photocanvas.configure(highlightthickness=0)
        #返回按钮
        self.backbtn = tk.Button(self.photocanvas,image = self.backimg,height=self.backbtnheight,width=self.backbtnwidth,command=self.back)
        self.backbtn.place(x=self.backbtnpadding,y=self.backbtnpadding) 
        self.Canvaslist = []
        self.pausebtnlist = []
        #图片缩略图放置
        for n in range(0,len(musiclist)):
            self.Canvaslist.append(tk.Canvas(self.photocanvas,bg="white", width=int(self.photowidth),height=int(self.photoheight)))
            self.Canvaslist[n].place(x=self.photomovex,y=n*(self.photoheight+self.photopadding)+self.topheight)
            self.Canvaslist[n].create_text(self.photowidth/2,self.photoheight/2,text="啊啊啊啊啊啊啊",font=("黑体",25))
            self.pausebtnlist.append(tk.Button(self.Canvaslist[n],image = self.playimg,width=self.pausebtnwidth,height=self.pausebtnwidth,command=self.returnfun(n)))
            self.pausebtnlist[n].place(x=self.pausebtnmovex,y=self.pausebtnmovey)
    def back(self):
        self.musicpage.destroy()
        #self.vbar.destory()
    #选中要播放的音乐
    def choosemusic(self,x):
        _thread.start_new_thread( self.playmusic, ("Thread", x))
        if x==self.curid:
            self.curid=-1
            self.pausebtnlist[x].config(image=self.playimg)
            return
        self.curid = x
        for n in range(0,len(self.pausebtnlist)):
            if n!=self.curid:
                self.pausebtnlist[n].config(image=self.playimg)
            else:
                self.pausebtnlist[n].config(image=self.pauseimg)
        # if self.curid!=-1:
        #     self.pausebtnlist[self.curid].config(image=self.playimg)
        # if self.curid!=x:
        #     self.curid = x
        #     self.pausebtnlist[x].config(image=self.pauseimg)
        # else:
        #     self.pausebtnlist[x].config(image=self.pauseimg)
        #locals()['self.temppausebtn'+str(x+1)].config(image=self.playimg)
    def returnfun(self,x):
        return lambda:self.choosemusic(x)
    #播放音乐
    def playmusic(self,threadname,x):
        filepath = "music/music1.mp3"
        py.mixer.init()
        # 加载音乐
        py.mixer.music.load(filepath)
        py.mixer.music.play(start=0.0)
        #播放时长，没有此设置，音乐不会播放，会一次性加载完
        time.sleep(300)
        py.mixer.music.stop()
    #暂停音乐
    def pausemusic(self,x):
        pass

if __name__ == '__main__':    
    root = tk.Tk()
    root.attributes("-fullscreen",True)
    winwidth = root.winfo_screenwidth()
    winheight = root.winfo_screenheight()
    photopage(root,winheight,winwidth)
    root.mainloop()