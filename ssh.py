import paramiko
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("go.eecis.udel.edu", port=22,username="searfmat",password="M@ttORH$2019")
stdin,stdout,stderr=ssh_client.exec_command("ls")
print(stdout.readlines())
ssh_client.close()

#ftp_client=ssh.open_sftp()
#ftp_client.put("localfilepath","remotefilepath")
#ftp_client.close()