from tkinter import *
import time
import os
root = Tk()

frames = [PhotoImage(file='loading.gif',format = 'gif -index %i' %(i)) for i in range(12)]

def update(ind):

    frame = frames[ind]
    if ind==11:
        ind=0
    else:
        ind += 1
    label.configure(image=frame)
    root.after(100, update, ind)

while True:
    label = Label(root)
    label.pack()
    root.after(0, update, 0)
    root.mainloop()