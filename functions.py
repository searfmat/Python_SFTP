import paramiko
from os import walk

dirList = []

def filesInDir(newDir):
    f = []
    i = 0
    for (dirpath, dirnames, filenames) in walk(newDir):
        f.extend(filenames)
        break
    while i < len(f):
        dirList.append(newDir + "/" + str(f[i]))
        i += 1

def getHost(host):
    global HOST
    HOST = host

def getPort(port):
    global PORT
    PORT = port
    
def getUser(user):
    global USER
    USER = user

def getPass(password):
    global PASSWORD
    PASSWORD = password
