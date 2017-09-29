import os,ftplib
from ftplib import FTP

def login(ip,username,password):
    global f

    try:
        f = FTP(ip)
        f.login(username,password)
    except ftplib.error_perm:
        print ("Can not login,Please check the username or password.")
        f.quit()
        return False
    else:
        print ("Login seccessfully.")
        return True

def changeDir(remoteFile):
    try:
        f.cwd(remoteFile)
    except ftplib.error_perm:
        print("Error: cannnot cd to '%s'" %remoteFile)
        f.quit()

    else:
        print("You have change to the '%s' folder" %remoteFile)


def uploadFiles(remoteFile,filename):
    changeDir(remoteFile)
    try:
        f.storbinary('STOR %s' %filename,open(filename,"rb"))
    except ftplib.error_perm:
        print("Error: can not read the file '%s'" %filename)
        f.quit()
    else:
        print("The file %s has been downloaded in %s." %(filename,remoteFile))



def uploadDir(remoteFile,filename,localFile):
    changeDir(remoteFile)
    try:
        f.mkd(filename)
    except ftplib.error_perm:
        print ("The file has been uploaded")
        f.quit()
        return
    remoteFile += "/" + filename
    try:
        os.chdir(localFile+"//"+filename)
        localFile=os.getcwd()
        filelist=os.listdir(localFile)
        print(localFile)
    except OSError:
        print("you get wrong system file path")

    for item in filelist:
        if os.path.isfile(item):
            uploadFiles(remoteFile, item)

    for item in filelist:
        if os.path.isdir(item):
            uploadDir(remoteFile, item, localFile)

if __name__=="__main__":
    host = "your host ip"
    username = "your account"
    password = "your ftp server password"
    filename = input("type a filename:")
    localFile = "c:\data"
    remoteFile = "/event"
    if login(host,username,password):
        uploadDir(remoteFile,filename,localFile)

