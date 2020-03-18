from tkinter import *  
from tkinter import filedialog


def track(var):
    print(var)
    return var

def fileopen():
    root.filename =  filedialog.askdirectory(initialdir = "/",title = "Select file",)
    newList.insert(1, root.filename)
    track(root.filename)

    
    
root = Tk()

root.geometry("400x500")

newList = Listbox(root, height=10, width=50)
dirButton = Button(root, text = "Add Directories", command = fileopen)

dirButton.place(x=160,y=10)
newList.place(x=50, y=50)


root.mainloop()
