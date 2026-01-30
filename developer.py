from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\hp\OneDrive\Desktop\college_images\240_F_116883786_wuckft1sNw1ouQfJ6FuquZnxea3qBlxy.jpg")
        img_top=img_top.resize((1530,720), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        #img_top1=Image.open(r"C:\Users\hp\OneDrive\Desktop\college_images\download (12).jpeg")
        #img_top1=img_top1.resize((200,200), Image.LANCZOS)
        #self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        #f_lbl=Label(main_frame,image=self.photoimg_top1)
        #f_lbl.place(x=300,y=0,width=200,height=200)

        #developer info
        dev_label=Label(main_frame,text="Hello my name is Divyanka",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I have created my own attendance system",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\college_images\download (13).jpeg")
        img2=img2.resize((500,390), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=320,width=500,height=400)





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()