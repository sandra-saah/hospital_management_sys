from asyncore import read, write
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv 
import random 
import time
import datetime
from tkinter import font
from turtle import down, width
import pandas as pd
from tkinter import *
from tkinter import filedialog, messagebox, ttk 
from setuptools import Command

import numpy as np
import sys 
from tkinter import * 
from tkinter.scrolledtext import ScrolledText
#create a window S.S
nw = tk.Tk()
nw.title("Infective Endocarditis Database")
nw.geometry("1350x700")

label_title = Label(nw,bd=20,relief=RIDGE,text="Infective Endocarditis Database",fg="black",bg="white",font=("helvetica",40,"bold"))
label_title.pack(side=TOP,fill=X)

 # ---------------- frame / Display data  -------------
        #Note book : the data will be displayed as notebook S.S
        # ie_notebook = ttk.Notebook(nw)
        # ie_notebook.pack(pady=15)

        # # section for the Note book / tables S.s
        # tb_frame1 = Frame(ie_notebook,bd=10,relief=RIDGE)
        # tb_frame1.place(x=0,y=105,width=1100,height=400)
        
        #  # section for the Note book / tables S.s
        # tb_frame2 = Frame(ie_notebook,bd=10,relief=RIDGE)
        # tb_frame2.place(x=0,y=105,width=1100,height=400)


        # ie_notebook.add(tb_frame1,text="GBS_AndIEDiagnosisforUWE")
        # ie_notebook.add(tb_frame2,text="NBT IE data for UWE")


        # #this section is for entering new data in the tables left side S.s
        # dataFrameInfo = LabelFrame(self.nw,bd=10,relief=RIDGE,font=("arial",12,"bold"),text="Information")
        # dataFrameInfo.place(x=0,y=501,width=1100,height=200)

class frames(): #create frames for each table displaying its data A.B
   
    
   ##1st Frame 
    ie_notebook = ttk.Notebook(nw)
    ie_notebook.pack(padx=15,pady=15)

    tb_frame1 = Frame(ie_notebook,bd=10,relief=RIDGE)
    tb_frame1.place(x=0,y=105,width=1100,height=400)

    filepath = r"GBS_AndIEDiagnosisforUWE.csv"
    df = pd.read_csv(filepath)
    cols = list(df.columns)
    tree = ttk.Treeview(tb_frame1)
    tree.pack()
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')
    for index, row in df.iterrows():
        tree.insert("",10,text=index,values=list(row))
    ie_notebook.add(tb_frame1,text="GBS and IE Diagnosis")

    scroll_x = ttk.Scrollbar(tb_frame1,orient=HORIZONTAL)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_x=ttk.Scrollbar(command=Canvas.xview)
    #2nd Frame

    tb_frame2 = Frame(ie_notebook,bd=10,relief=RIDGE)
    tb_frame2.place(x=0,y=105,width=1100,height=400)
    filepath = r"NBT_IE_data_for_UWE.csv"
    df = pd.read_csv(filepath)
    cols = list(df.columns)
    tree = ttk.Treeview(tb_frame2)
    tree.pack()
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')
    for index, row in df.iterrows():
        tree.insert("",1000,text=index,values=list(row))
    ie_notebook.add(tb_frame2,text="NBT and IE")

    #3rd Frame

    tb_frame3 = Frame(ie_notebook,bd=10,relief=RIDGE)
    tb_frame3.place(x=0,y=105,width=1100,height=400)
    filepath = r"SA_AndIEDiagnosis_for_UWE.csv"
    df = pd.read_csv(filepath)
    cols = list(df.columns)
    tree = ttk.Treeview(tb_frame3)
    tree.pack()
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')
    for index, row in df.iterrows():
        tree.insert("",1000,text=index,values=list(row))
    
    ie_notebook.add(tb_frame3,text="SA and IE Diagnosis")

    #4th Frame:

    tb_frame4 = Frame(ie_notebook,bd=10,relief=RIDGE)
    tb_frame4.place(x=0,y=105,width=1100,height=400)
    ##THIS file IS DIFFERENT THAN THE OTHERS it's not a csv,that's why we used xlsx at the end instead od csv
    df = pd.read_excel(r"StrepAndIEDiagnosisfor_UWE.xlsx")
    cols = list(df.columns)
    tree = ttk.Treeview(tb_frame4)
    tree.pack()
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')
    for index, row in df.iterrows():
        tree.insert("",1000,text=index,values=list(row))     
    ie_notebook.add(tb_frame4,text="Strep and IE Diagnosis")
    
    #5th Frame

    tb_frame5 = Frame(ie_notebook,bd=10,relief=RIDGE)
    tb_frame5.place(x=0,y=105,width=1100,height=400)
    filepath = r"UHB_IE_data_for_UWE.csv"
    df = pd.read_csv(filepath)
    cols = list(df.columns)
    tree = ttk.Treeview(tb_frame5)
    tree.pack()
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')
    for index, row in df.iterrows():
        tree.insert("",1000,text=index,values=list(row))
    
    ie_notebook.add(tb_frame5,text="UHB and IE")

class buttons1:
                #Section for multiple buttons right side S.s
        btnFrame = LabelFrame(nw,bd=10,relief=RIDGE,font=("arial",12,"bold"),text="Options")
        btnFrame.place(x=25,y=409,width=1300,height=100)

        # Buttons data S.s
        Update_btn = Button(btnFrame,text="Update",bg="green",fg='black',font=("arial",12,"bold"),width=22,height=2)
        Update_btn.grid(row=0,column=0)

        Delete_btn = Button(btnFrame,text="Delete",bg="green",fg='black',font=("arial",12,"bold"),width=22,height=2)
        Delete_btn.grid(row=0,column=1)

        view_data_btn = Button(btnFrame,text="View data",bg="green",fg='black',font=("arial",12,"bold"),width=22,height=2)
        view_data_btn.grid(row=0,column=2)

        csv_btn = Button(btnFrame,text="Import CSV file",bg="green",fg='black',font=("arial",12,"bold"),width=22,height=2)
        csv_btn.grid(row=0,column=3)

class information():
        #this section is for entering new data in the tables left side S.s
        dataFrameInfo = LabelFrame(nw,bd=10,relief=RIDGE,font=("arial",12,"bold"),text="Information")
        dataFrameInfo.place(x=25,y=501,width=1300,height=200)
        
        #create a scroll bar for information Box S.S
        text_scroll = Scrollbar(dataFrameInfo)
        text_scroll.pack(side=RIGHT,fill = Y)
        #Create text box
        my_text = Text(dataFrameInfo,width=1100,height=200,font=("Helvetica0",16),selectbackground="yellow",yscrollcommand=text_scroll.set)
        my_text.pack()
        
        #configure our scrollbar
        text_scroll.config(command=my_text.yview)
       


if __name__ == "__main__":
    
    nw.resizable(False,False)
    nw.mainloop()