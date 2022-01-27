from operator import truediv
from os import access
import cv2
import dropbox
import time
import random

def take_snapshot():
    number = random.randint(0,100)
    #starting camera by initialising cv2 library
    videocaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #click the picture while camera is on
        ret,frame = videocaptureObject.read()
        #save the imgae on the computer by creating the file name
        #imwrite is used to save the image
        img_name = "img" + str(number) + ".jpg"
        cv2.imwrite(img_name,frame)
        result = False
    print("Picture Clicked")
    #releasing the camera
    videocaptureObject.release()
    #close all the windows that might have opened during this process
    cv2.destroyAllWindows()
    return img_name

def upload_file(img_name):
    access_token = 'qrwcc6KWrjgAAAAAAAAAAcKN9Ci-mXLWi8j4CpUdH-BG4ZUkGLslYXeh4J_GZxMC'
    file_name = img_name
    file_from = file_name
    file_to = "/class102/" + img_name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File has been uploaded")

def main():
    start_time = time.time()
    while(True):
        if((time.time()-start_time)>20):
            start_time = time.time()
            name = take_snapshot()
            upload_file(name)

main()
