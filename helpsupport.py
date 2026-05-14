from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.title("Attendance Management System Using Face Recognition")

# This part is image labels setting start 
        # first header image  
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

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        bg1=bg1.resize((self.screen_width,self.screen_height),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=banner_height,width=self.screen_width,height=self.screen_height)


        #title section
        title_lb1 = Label(bg_img,text="Assistance",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=self.screen_width,height=40)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/web.png")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=250,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/fb.png")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="LINKDIN",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=480,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/yt.png")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=710,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=940,y=380,width=180,height=45)


        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = "http://www.stemsquare.vn/"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/sahil-siwach-060b88258"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/channel/UCzmueccz-WuanzMaJ1ds1Tg"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()