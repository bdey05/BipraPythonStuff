from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Codemy.com Image Viewer")
root.iconbitmap("ogbro.ico")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box or you die!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
