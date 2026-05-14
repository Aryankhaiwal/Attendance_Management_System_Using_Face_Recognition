from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.title("Load Data")

        # This part is image labels setting start 
        img=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/banner.png")
        banner_height = int(self.screen_width * 120 / 1250)
        img = img.resize((self.screen_width, banner_height), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        #f_lb1.place(x=0,y=0,width=1250,height=120)
        #f_lb1.place(x=0,y=0,relwidth=1,height=120)
        f_lb1.place(x=0,y=0,relwidth=1,height=banner_height)

        # backgorund image 
        bg1=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/bg3.jpeg")

        #screen_width = self.root.winfo_screenwidth()
        #screen_height = self.root.winfo_screenheight()

        bg1=bg1.resize((self.screen_width,self.screen_height),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=banner_height,width=self.screen_width,height=self.screen_height-banner_height)


        #title section
        title_lb1 = Label(bg_img,text="Load Face Data",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(relx=0,rely=0,relwidth=1,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/t_btn1.png")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(relx=0.42,rely=0.20,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Load Data",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(relx=0.42,rely=0.42,width=180,height=45)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/data_img"
        # FIX FOR FIRST ERROR (ensure folder exists)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        #data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir) if file.endswith(".jpg")]
        
        faces=[]
        ids=[]

        for image in path:
            try:
                img=Image.open(image).convert('L')
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])
            except:
                continue

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Load Data",imageNp)
            cv2.waitKey(1)
            #cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Data loaded successfully!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()