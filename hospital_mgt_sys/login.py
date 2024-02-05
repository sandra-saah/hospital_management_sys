from tkinter import * 
import tkinter as tk
from tkinter import messagebox
import csv 
from window_N import nw

class User:
    def __init__(self):
        self.role = 0
        self.username = ""
        self.password = ""

user = User()



def btn_clicked():
        if user.username == "" or user.password =="":
            messagebox.showerror("Error",'Enter all the information')
        else:
            x = 0
            with open('Users.csv','r') as csv_f:
                c = list(csv.reader(csv_f))
                for row in c:
                    if x == 0:
                        for v in row:
                            if v == user.username and row[1] == user.password and x ==0:
                                messagebox.showinfo("Success","Login Success!")
                                newWindow = Toplevel(window)
                                x = 1
                            else :
                                messagebox.showerror('Invalid Credential','Invalid Username or Password')



#login page setup 
window = Tk()
window.geometry("1350x700")
window.configure(bg = '#093545' )
canvas = Canvas(
    window,
    bg = "#093545",
    height = 700,
    width = 1350,
    bd = 0,
    highlightthickness= 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth= 0,
    highlightthickness= 0,
    command = nw,
    relief = "flat"
)
b0.place(
    x = 490, y=485,
    width = 300,
    height = 45
)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    640.0, 426.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#224957",
    fg = "white",
    highlightthickness = 0)

entry0.place(
    x = 500.0, y = 404,
    width = 280.0,
    height = 43)

canvas.create_text(
    543.5, 427.0,
    text = "Password",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(14.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    640.0, 347.5,
    image = entry1_img)

entry2_bg = canvas.create_image(
    640.0, 268.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#224957",
    fg = "white",
    highlightthickness = 0)

entry1.place(
    x = 500.0, y = 325,
    width = 280.0,
    height = 43)

entry1.insert(0, "Username")
entry0.insert(0, "Password")

#select the role
n = tk.StringVar(window)
n.set("Select Role")
options_list = ["Doctor", "Admin"]
entry2 = tk.OptionMenu(window, n, *options_list)
entry2.pack()
  
entry2.configure(bg="#224957", bd=0, fg="white", highlightthickness = 0)
  
entry2.place(
    x = 500.0, y = 246,
    width = 280.0,
    height = 43)

canvas.create_text(
    548.0, 348.0,
    text = "Username",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(16.0)))

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    640.0, 360.0,
    image=background_img)

canvas.create_text(
    639.5, 179.0,
    text = "Sign in to Infective Endocarditis Database",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(18.0)))

canvas.create_text(
    640.0, 88.5,
    text = "Sign in",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(64.0)))



window.resizable(False,False)
window.mainloop()
