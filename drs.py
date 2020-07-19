import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import imutils
import time


stream= cv2.VideoCapture("clip.mp4")
def play(speed):
    print(f" You clicked play . speed is {speed}")

         # play the video in forward mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    
        
    grabbed, frame = stream.read()   #to read the frame from stream

    if not grabbed:
        exit()

    frame= imutils.resize(frame , width=SET_WIDTH, height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)





def pending(decission):
    #1.display decission pending image
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)

    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    
    #2.wait for 1 second
    time.sleep(1)

    #3.display sponsor 
    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)

    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    #4.what for 1.5 second
    time.sleep(1.5)

    #5. display out or not out 
    if decission== "out":
        decissionImg="out.png"
    else:
        decissionImg="not_out.png"
    frame = cv2.cvtColor(cv2.imread(decissionImg),cv2.COLOR_BGR2RGB)

    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    canvas.create_text(132,29,fill="red",font="Times 26 blod",text="Decission Pending")


def out():
    thread=threading.Thread(target=pending, args=("out",))
    thread.daemon=1
    thread.start()    

def not_out():
    thread=threading.Thread(target=pending, args=("Not out",))
    thread.daemon=1
    thread.start()
  

#width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

#tkinter gui starts here
window=tkinter.Tk()
window.title("MR Third Umpire Decission Review Kit")

cv_img = cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
cv_img = imutils.resize(cv_img,width=SET_WIDTH,height=SET_HEIGHT)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)

photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas= canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()


#butons to control playback
btn = tkinter.Button(window, text="<< Previous(fast)",width=50,command=partial(play,-25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous(slow)",width=50,command=partial(play,-2))
btn.pack()

btn = tkinter.Button(window, text=" Next(slow) >>",width=50,command=partial(play,2))
btn.pack()

btn = tkinter.Button(window, text=" Next(fast) >>",width=50,command=partial(play,25))
btn.pack()

btn = tkinter.Button(window, text="Give OUT",width=50,command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out",width=50,command=not_out)
btn.pack()
window.mainloop()

