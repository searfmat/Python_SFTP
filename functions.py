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
        print(dirList)
        i += 1

def getHost(host):
    global HOST
    HOST = host
    print(HOST)

def getPort(port):
    global PORT
    PORT = port
    print(PORT)
    
def getUser(user):
    global USER
    USER = user
    print(USER)

def getPass(password):
    global PASSWORD
    PASSWORD = password
    print(PASSWORD)
