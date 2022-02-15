import tkinter
from tkinter import *
import random
from tkinter import messagebox

# you can add more words as per your requirement
answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "zzlepu"
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    "puzzle"
]

# I have improvised the code by using len(words)
num =  random.randrange(0, len(words), 1)

def default():
    global words,answers,num
    lbl.config(text = words[num])

def res():
    global words,answers,num
    num = random.randrange(0, len(words), 1)
    lbl.config(text = words[num])
    e1.delete(0, END)


def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        res()
    else:
        messagebox.showerror("In Correct", "This is not Correct")
        e1.delete(0, END)




root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Make Words")
root.configure(background = "#000000")

lbl = Label(
    root,
    text = "Your here",
    font = ("Lato", 18),
    bg = "#000000",
    fg = "#FFFFFF",
)
lbl.pack(pady = 30,ipady=10,ipadx=10)


ans1 = StringVar()
e1 = Entry(
    root,
    font = ("Lato", 16),
    textvariable = ans1,
)
e1.pack(ipady=5,ipadx=5)

btncheck = Button(
    root,
    text = "Check",
    font = ("Roboto", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#6ab04c",
    relief = GROOVE,
    command = checkans,
)
btncheck.pack(pady = 40)

btnreset = Button(
    root,
    text = "Reset",
    font = ("Roboto", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = res,
)
btnreset.pack()

default()
root.mainloop()