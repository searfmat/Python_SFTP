from tkinter import *  
from tkinter import filedialog
import functions
import ssh

def fileopen():
    root.filename =  filedialog.askdirectory(initialdir = "/",title = "Select file",)
    newList.insert(1, root.filename)
    functions.fileListAdd(root.filename)

def send():
    functions.getHost(newHost.get())
    functions.getPort(newPort.get())
    functions.getUser(newUsername.get())
    functions.getPass(newPassword.get())
    ssh.ssh()


root = Tk()

root.geometry("400x500")

newHost = Entry(root)
newPort = Entry(root, width=5)
newUsername = Entry(root)
newPassword = Entry(root)
newList = Listbox(root, height=10, width=50)
dirButton = Button(root, text = "Add Directories", command = fileopen)
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
