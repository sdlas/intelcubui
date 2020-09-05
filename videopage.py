import tkinter as tk
import tkinter.colorchooser
import pygame as py
import time
import _thread
from tkinter import *
import cv2
from PIL import Image, ImageTk
import multiprocessing

window_width=960
window_height=620
image_width=320
image_height=int(window_height*1)
imagepos_x=0
imagepos_y=0
butpos_x=450
butpos_y=450

class videopage():
    def __init__(self,master,winheight,winwidth):
        self.master = master
        self.master.config(bg='blue')
        self.face1 = tk.Frame(self.master,)
        self.face1.pack()
        self.vc1 = cv2.VideoCapture('dance.mp4')
        #self.face1.geometry(str(window_width)+'x'+str(window_height))
        self.canvas1 =tk.Canvas(self.face1,bg='white',width=image_width,height=image_height)
        self.canvas1.pack()
        self.video()
        # p1 = multiprocessing.Process(target=self.video)
        # p1.start()
    #图像转换，用于在画布中显示
    def tkImage(self,vc):
        ref,frame = vc.read()
        cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pilImage = Image.fromarray(cvimage)
        pilImage = pilImage.resize((image_width, image_height),Image.ANTIALIAS)
        tkImage =  ImageTk.PhotoImage(image=pilImage)
        return tkImage
    #图像的显示与更新
    def video(self,):
        def video_loop():
            try:
                while True:
                    picture1=self.tkImage(self.vc1)
                    self.canvas1.create_image(0,0,anchor='nw',image=picture1)  
                    #canvas4.create_image(0,0,anchor='nw',image=picture1) 
                    self.face1.update_idletasks()  #最重要的更新是靠这两句来实现
                    self.face1.update()
            except:
                self.back()
            
        video_loop()
        #self.face1.mainloop()
        self.vc1.release()
        cv2.destroyAllWindows()
    def back(self):
        self.face1.destroy()