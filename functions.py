import paramiko

dirList = []

def fileListAdd(newDir):
    dirList.append(newDir)

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
