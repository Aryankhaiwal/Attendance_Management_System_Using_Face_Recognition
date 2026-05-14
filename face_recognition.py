# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from tkinter import filedialog
from time import strftime
from datetime import datetime
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.title("Attendance Management System Using Face Recognition")

        # This part is image labels setting start 
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
        title_lb1 = Label(bg_img,text="Welcome to the face recognition system",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(relx=0,rely=0,relwidth=1,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(relx=0.5,rely=0.30,anchor="center",width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Recognition",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(relx=0.5,rely=0.44,anchor="center",width=180,height=45)
        img_btn = Button(bg_img, command=self.recognize_image,
                 text="Image Recognition",
                 cursor="hand2",
                 font=("tahoma",15,"bold"),
                 bg="white", fg="navyblue")

        img_btn.place(relx=0.5, rely=0.52, anchor="center", width=180, height=45)
    #=====================Attendance===================

    def mark_attendance(self, i, r, n):
        import os

        # create file if it doesn't exist
        if not os.path.exists("attendance.csv"):
            open("attendance.csv", "w").close()

        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            entry_list = []

            for line in myDataList:
                entry = line.strip().split(",")

                # skip empty or incomplete rows
                if len(entry) >= 5:
                    entry_list.append((entry[0], entry[4]))

            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")

            # mark attendance only once per day
            if (str(i), d1) not in entry_list:
                f.writelines(f"\n{i},{r},{n},{dtString},{d1},Present")



    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))

                conn = mysql.connector.connect(username='root', password='sahil@123',host='localhost',database='face_recognition',port=3306)
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID="+str(id))
                n = cursor.fetchone()
                n = n[0] if n else "Unknown"

                cursor.execute("select Roll_No from student where Student_ID="+str(id))
                r = cursor.fetchone()
                r = r[0] if r else "Unknown"

                cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i = cursor.fetchone()
                i = i[0] if i else "Unknown"


                if confidence > 85:
                    cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll-No:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,h]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        if not os.path.exists("clf.xml"):
            messagebox.showerror("Error","Please train the model first!")
            return
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img = videoCap.read()
            if not ret:
                break
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Recognition",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()

    def recognize_image(self):
        file_path = filedialog.askopenfilename()

        if file_path == "":
            return

        # Load image
        img = cv2.imread(file_path)
        if img is None:
            messagebox.showerror("Error", "Invalid image file")
            return

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        if not os.path.exists("clf.xml"):
            messagebox.showerror("Error", "Please train the model first!")
            return
        clf.read("clf.xml")

        faces = faceCascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            messagebox.showerror("Error", "No face detected in image")
            return

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]

            id, predict = clf.predict(face)
            confidence = int(100 * (1 - predict / 300))

            conn = mysql.connector.connect(
                username='root', password='sahil@123',
                host='localhost', database='face_recognition', port=3306
            )
            cursor = conn.cursor()

            cursor.execute("select Name from student where Student_ID="+str(id))
            n = cursor.fetchone()
            n = n[0] if n else "Unknown"

            cursor.execute("select Roll_No from student where Student_ID="+str(id))
            r = cursor.fetchone()
            r = r[0] if r else "Unknown"

            cursor.execute("select Student_ID from student where Student_ID="+str(id))
            i = cursor.fetchone()
            i = i[0] if i else "Unknown"

            if confidence > 80:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)

                # OPTIONAL: mark attendance
                self.mark_attendance(i, r, n)

            else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                cv2.putText(img,"Unknown",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)

        cv2.imshow("Image Recognition", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()