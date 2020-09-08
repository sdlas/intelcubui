import tkinter as tk
import tkinter.colorchooser
import pygame as py
import time
import _thread
from tkinter import *
import cv2
from PIL import Image, ImageTk
import multiprocessing
import glob

class title():
    def __init__(self,master,_winheight,_winwidth,str):
        self.winheight = _winheight
        self.winwidth = _winwidth
        self.master =master
        self.topheight = 130 #顶部标题高度
        self.titleheight = self.topheight/2
        self.titlewidth = self.titleheight*5
        self.titlepadding = self.topheight/4 #顶部按钮的间距
        self.backimg = ImageTk.PhotoImage(Image.open("srcimage/"+str+".jpg").resize((int(self.titlewidth),int(self.titleheight)))) 
        self.title = tk.Button(self.master,image = self.backimg,height=self.titleheight,width=self.titlewidth,command=self.passit,bd=0)
        self.title.place(x=(self.winwidth-self.titlewidth)/2,y=self.titlepadding) 
    def passit(self):
        pass