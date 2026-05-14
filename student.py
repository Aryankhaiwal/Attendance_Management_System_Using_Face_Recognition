import os
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkcalendar import DateEntry
# Testing Connection 
"""
conn = mysql.connector.connect(username='root', password='sahil@123',host='localhost',database='face_recognition',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Student:
    def __init__(self,root):
        self.root=root
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.title("Attendance Management System Using Face Recognition")

        #-----------Variables-------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_day = StringVar()
        self.var_month = StringVar()
        self.var_dob_year = StringVar()

    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/banner.png")
        banner_height = int(self.screen_width * 120 / 1250)
        img=img.resize((self.screen_width,banner_height),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=self.screen_width,height=banner_height)

        # backgorund image 
        bg1=Image.open(r"/Users/sahil/Downloads/Attendance_Management_System_Using_Face_Recognition-main/Images_GUI/bg3.jpeg")
        bg1=bg1.resize((self.screen_width,self.screen_height),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=banner_height,width=self.screen_width,height=self.screen_height)
        bg_img.lower()


        #title section
        title_lb1 = Label(bg_img,text="Student Information Management Page",font=("verdana",25,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=self.screen_width,height=40)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(relx=0,rely=0.05,relwidth=1,relheight=0.75)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Information",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(relx=0.01,rely=0.02,relwidth=0.48,relheight=0.95)

        # Current Course 
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",10,"bold"),fg="navyblue")
        current_course_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.30)
        current_course_frame.columnconfigure((0,1,2,3), weight=1)

        #label Department
        dep_label=Label(current_course_frame,text="Major",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select","Software Engineering","Information Security","Business Administration", "Digital Media Design"

)
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky="ew")

        # -----------------------------------------------------

        #label Course
        cou_label=Label(current_course_frame,text="Subject",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        cou_label.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        #combo box 
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=15,font=("verdana",12,"bold"),state="readonly")
        cou_combo["values"]=( "Select", "STEM","Multimedia Graphics","Network Programming","Linux","AI")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=5,pady=15,sticky="ew")

        #-------------------------------------------------------------

        #label Year
        year_label=Label(current_course_frame,text="Year",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=0,padx=10,pady=15,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select","2020","2021","2022","2023","2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky="ew")

        #-----------------------------------------------------------------

        #label Semester 
        year_label=Label(current_course_frame,text="Semester",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=2,padx=10,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select","Semester 1","Semester 2")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=5,pady=15,sticky="ew")

        #Class Student Information
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Overview",font=("verdana",12,"bold"),fg="navyblue")
        class_Student_frame.place(relx=0.01, rely=0.32, relwidth=0.98, relheight=0.47)
        class_Student_frame.columnconfigure(0, weight=1)
        class_Student_frame.columnconfigure(1, weight=2)
        class_Student_frame.columnconfigure(2, weight=1)
        class_Student_frame.columnconfigure(3, weight=2)
        class_Student_frame.columnconfigure(4, weight=1)
        class_Student_frame.columnconfigure(5, weight=1)

        #Student id
        studentId_label = Label(class_Student_frame,text="ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=8,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=8,sticky="ew")

        #Student name
        student_name_label = Label(class_Student_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=8,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=8,sticky="ew")

        #Class Didvision
        student_div_label = Label(class_Student_frame,text="Class session:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_div_label.grid(row=1,column=0,padx=10,pady=8,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=13,font=("verdana",12,"bold"),state="readonly")
        div_combo["values"]=("Morning","Afternoon")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=8,sticky="ew")

        #Roll No
        student_roll_label = Label(class_Student_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=2,padx=10,pady=8,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=10,pady=8,sticky="ew")

        # ================= Gender =================
        student_gender_label = Label(
            class_Student_frame,
            text="Gender:",
            font=("verdana",12,"bold"),
            fg="navyblue",
            bg="white"
        )
        student_gender_label.grid(row=5,column=0,padx=10,pady=8,sticky=W)

        gender_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_gender,
            state="readonly",
            font=("verdana",12,"bold")
        )
        gender_combo["values"] = ("Male","Female","Other")
        gender_combo.current(0)

        gender_combo.grid(row=5,column=1,padx=10,pady=8,sticky="ew")


        # ================= DOB =================

        student_dob_label = Label(
        class_Student_frame,
        text="DOB:",
        font=("verdana",12,"bold"),
        fg="navyblue",
        bg="white"
        )
        student_dob_label.grid(row=6,column=0,padx=10,pady=8,sticky=W)

        # Day

        day_combo = ttk.Combobox(
        class_Student_frame,
        textvariable=self.var_day,
        width=5,
        state="readonly"
        )
        day_combo["values"] = ["Day"] + list(range(1,32))
        day_combo.current(0)
        day_combo.grid(row=6,column=1,padx=3,pady=8,sticky="ew")

        # Month

        month_combo = ttk.Combobox(
        class_Student_frame,
        textvariable=self.var_month,
        width=6,
        state="readonly"
        )
        month_combo["values"] = ["Month","Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"]
        month_combo.current(0)
        month_combo.grid(row=6,column=2,padx=3,pady=8,sticky="ew")

        # Year

        year_combo = ttk.Combobox(
        class_Student_frame,
        textvariable=self.var_dob_year,
        width=6,
        state="readonly"
        )
        year_combo["values"] = ["Year"] + list(range(1980,2026))
        year_combo.current(0)
        year_combo.grid(row=6,column=3,padx=3,pady=8,sticky="ew")


        #Email
        student_email_label = Label(class_Student_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=3,column=0,padx=10,pady=8,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=10,pady=8,sticky="ew")

        #Phone Number
        student_mob_label = Label(class_Student_frame,text="Mobile:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_mob_label.grid(row=3,column=2,padx=10,pady=8,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob,width=15,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=3,column=3,padx=10,pady=8,sticky="ew")

        #Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_address_label.grid(row=4,column=0,padx=10,pady=8,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=10,pady=8,sticky="ew")

        #Teacher Name
        student_tutor_label = Label(class_Student_frame,text="Lecturer:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_tutor_label.grid(row=4,column=2,padx=10,pady=8,sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("verdana",12,"bold"))
        student_tutor_entry.grid(row=4,column=3,padx=10,pady=8,sticky="ew")

        # Radio Buttons

        self.var_radio1 = StringVar()

        radiobtn1 = ttk.Radiobutton(
            class_Student_frame,
            text="Take Photo",
            variable=self.var_radio1,
            value="Yes"
        )
        radiobtn1.grid(row=7, column=0, padx=10, pady=10, sticky=W)


        radiobtn2 = ttk.Radiobutton(
            class_Student_frame,
            text="No Image",
            variable=self.var_radio1,
            value="No"
        )
        radiobtn2.grid(row=7, column=2, padx=10, pady=10, sticky=W)

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(relx=0.02,rely=0.80,relwidth=0.96,relheight=0.15)
        btn_frame.grid_propagate(False)
        btn_frame.lift()


        # ===== Row 1 =====
        save_btn = Button(btn_frame, command=self.add_data, text="Save",
                        font=("Segoe UI",12,"bold"),
                        width=16,
                        bg="#0b6e3c", fg="black",
                        activebackground="#2ecc71", cursor="hand2")
        save_btn.grid(row=0, column=0, padx=15, pady=8)

        update_btn = Button(btn_frame, command=self.update_data, text="Edit",
                            font=("Segoe UI",12,"bold"),
                            width=16,
                            bg="#0b6e3c", fg="black",
                            activebackground="#2ecc71", cursor="hand2")
        update_btn.grid(row=0, column=1, padx=15, pady=8)

        del_btn = Button(btn_frame, command=self.delete_data, text="Delete",
                        font=("Segoe UI",12,"bold"),
                        width=16,
                        bg="#0b6e3c", fg="black",
                        activebackground="#2ecc71", cursor="hand2")
        del_btn.grid(row=0, column=2, padx=15, pady=8)

        # ===== Row 2 =====
        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset",
                        font=("Segoe UI",12,"bold"),
                        width=16,
                        bg="#0b6e3c", fg="black",
                        activebackground="#2ecc71", cursor="hand2")
        reset_btn.grid(row=1, column=0, padx=15, pady=8)

        take_photo_btn = Button(btn_frame, command=self.generate_dataset, text="Take Photo",
                                font=("Segoe UI",12,"bold"),
                                width=16,
                                bg="#0b6e3c", fg="black",
                                activebackground="#2ecc71", cursor="hand2")
        take_photo_btn.grid(row=1, column=1, padx=15, pady=8)

        update_photo_btn = Button(btn_frame, text="Edit Photo",
                                font=("Segoe UI",12,"bold"),
                                width=16,
                                bg="#0b6e3c", fg="black",
                                activebackground="#2ecc71", cursor="hand2")
        update_photo_btn.grid(row=1, column=2, padx=15, pady=8)
        btn_frame.update_idletasks()





        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="List",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(relx=0.51,rely=0.02,relwidth=0.48,relheight=0.95)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.15)
        search_frame.grid_propagate(False)
        search_frame.columnconfigure(0, weight=1)
        search_frame.columnconfigure(1, weight=2)
        search_frame.columnconfigure(2, weight=3)
        search_frame.columnconfigure(3, weight=1)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=( "Choose","Roll-No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10,sticky="ew")

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky="ew")

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="black",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=10,pady=10,sticky="ew")

        """ showAll_btn=Button(search_frame,command=self.fetch_data,text="Tất cả",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W) """

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(relx=0.02,rely=0.18,relwidth=0.96,relheight=0.75)
        table_frame.grid_propagate(False)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("ID","Name","Dep","Course","Year","Sem","Div","Gender","DOB","Mob-No","Address","Roll-No","Email","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Dep",text="Major")
        self.student_table.heading("Course",text="course")
        self.student_table.heading("Year",text="year")
        self.student_table.heading("Sem",text="semester")
        self.student_table.heading("Div",text="div")
        self.student_table.heading("Gender",text="gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Mob-No",text="Mob-No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Roll-No",text="Roll-No")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"


        # Set Width of Colums 
        self.student_table.column("ID",width=20)
        self.student_table.column("Name",width=100)
        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Mob-No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        self.root.update_idletasks()
# ==================Function Decleration==============================
    def add_data(self):
        if (self.var_dep.get()=="Select" or
            self.var_course.get()=="Select" or
            self.var_year.get()=="Select" or
            self.var_semester.get()=="Select" or
            self.var_std_id.get()=="" or
            self.var_std_name.get()=="" or
            self.var_div.get()=="" or
            self.var_roll.get()=="" or
            self.var_gender.get()=="" or
            self.var_email.get()=="" or
            self.var_mob.get()=="" or
            self.var_address.get()=="" or
            self.var_teacher.get()=="" or
            self.var_day.get()=="Day" or
            self.var_month.get()=="Month" or
            self.var_dob_year.get()=="Year"):
                messagebox.showerror("Error","Please fill all required fields including DOB!",parent=self.root)
                return
        else:
            try:
                conn = mysql.connector.connect(user='root', password='sahil@123',host='localhost',database='face_recognition',port=3306)
                dob_value = f"{self.var_day.get()}-{self.var_month.get()}-{self.var_dob_year.get()}"
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_div.get(),
                self.var_gender.get(),
                dob_value,
                self.var_mob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All records have been saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='sahil@123',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_roll.set(data[11]),
        self.var_email.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_dep.get()=="Select" or self.var_course.get()=="Select" or self.var_year.get()=="Select" or self.var_semester.get()=="Select" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please fill in all the required fields!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to edit it?",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='sahil@123',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Update successful!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID is required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete it?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='sahil@123',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted Successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set(""),
        self.var_course.set(""),
        self.var_year.set(""),
        self.var_semester.set(""),
        self.var_div.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='sahil@123',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT Student_ID,Name,Department,Course,Year,Semester,Division,Gender,DOB,Mobile_No,Address,Roll_No,Email,Teacher_Name,PhotoSample FROM student WHERE Roll_No=%s"
                my_cursor.execute(sql,(self.var_search.get(),))
                # my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select" or self.var_course.get()=="Select" or self.var_year.get()=="Select" or self.var_semester.get()=="Select" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please fill in all the required fields!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(user='root', password='sahil@123',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id = self.var_std_id.get()

                mycursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() 
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                if not os.path.exists("data_img"):
                    os.makedirs("data_img")
                cap=cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path=os.path.join("data_img","student."+str(id)+"."+str(img_id)+".jpg")
                        # file_path="data_img/student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset creation completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
