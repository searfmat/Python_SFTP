from tkinter import *  
from tkinter import filedialog
import execute

def fileopen():
    root.filename =  filedialog.askdirectory(initialdir = "/",title = "Select file",)
    newList.insert(1, root.filename)
    #for testing only
    print(root.filename)
    execute.printFunc(2)
    return root.filename

#for testing only
def send():
    print(newHost.get())
    print(newHost.get())
    print(newUsername.get())
    print(newPassword.get())
    return newHost.get(), newHost.get(), newUsername.get(), newPassword.get()


root = Tk()

root.geometry("400x500")

newHost = Entry(root)
newPort = Entry(root, width=5)
newUsername = Entry(root)
newPassword = Entry(root)
newList = Listbox(root, height=10, width=50)
dirButton = Button(root, text = "Add Directories", command = fileopen)
#sendTest is for testing only
sendButton = Button(root, text = "Transfer", command= send)
userLabel = Label(root, text= "Enter username:")
passLabel = Label(root, text= "Enter password:")
portLabel = Label(root, text= "Port:")
hostLabel = Label(root, text= "Hostname:")

dirButton.place(x=160, y=10)
newList.place(x=50, y=50)
hostLabel.place(x=75, y=225)
newHost.place(x=75, y=250)
portLabel.place(x=235, y=225)
newPort.place(x=235, y=250)
userLabel.place(x=140, y=275)
newUsername.place(x=140, y=300)
passLabel.place(x=140, y=325)
newPassword.place(x=140, y=350)
sendButton.place(x=170, y=400)


root.mainloop()
