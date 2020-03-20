import paramiko
import functions

def ssh():
    i = 0

    ssh_client =paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(functions.HOST, port=functions.PORT,username=functions.USER,password=functions.PASSWORD)

    stdin,stdout,stderr=ssh_client.exec_command("ls")
    stdin,stdout,stderr=ssh_client.exec_command("mkdir filetransfer | cd filetransfer")
    print(stdout.readlines())
    
    ftp_client=ssh_client.open_sftp()

    for i in range(len(functions.dirList)):
        fileLast = str(functions.dirList[i])
        fileLast.split("/")
        ftp_client.put(str(functions.dirList[i]),"filetransfer/" + fileLast[-1])

    stdin,stdout,stderr=ssh_client.exec_command("ls")
    print(stdout.readlines())

    ftp_client.close()
    ssh_client.close()
    