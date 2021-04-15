from tkinter import *
from PIL import Image,ImageTk
import os
import cv2
from tkinter import filedialog
from lane import videoLanes

def open_image():
    x=openfilename()
    result=videoLanes(x)
def openfilename(): 
    filename = filedialog.askopenfilename(title ='open') 
    return filename 

window=Tk()
window.title("load video")
window.config(bg='skyblue')
window.geometry('300x300')
l1=Label(window,text='Please upload the video by clicking the below button').pack()
b1=Button(window,text="Please upload the video",command=open_image)
b1.pack(padx=20,pady=20)
window.mainloop()

