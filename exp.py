from tkinter import *  
from tkinter import filedialog

root = Tk()
newList = Listbox(root)

root.geometry("500x500")


def fileopen():
    root.filename =  filedialog.askdirectory(initialdir = "/",title = "Select file",)
    newList.insert(1, root.filename)
    

myButton = Button(root, text = "Open", command = fileopen)
myButton.pack()
var = StringVar()
var.set("File1")


drop = OptionMenu(root, var, "File1","File2","File3")
drop.pack()
newList.pack()


myButton = Button(root)
root.mainloop()
