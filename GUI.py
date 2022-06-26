import tkinter as tk
import os
import time
from tkinter import messagebox
from PIL import ImageTk, Image




#os.system("powershell Start-Process powershell ")


window=tk.Tk()
window.geometry("1000x700")
window.title("Cnkd 2.0".center(250))
window.resizable(False, False)
img=(Image.open('capybara.jpg'))
resized_img=img.resize((400,300))
resized_img_=ImageTk.PhotoImage(resized_img)
label = tk.Label(window, image=resized_img_)
label.grid(row=0,column=1)



message_box=tk.Text()
readme=open("readme.txt", "r")
read_me=readme.read()
message_box.insert("1.0",read_me)
message_box.grid(row=2, column=2)



second=tk.StringVar()
second.set("05")
minute=tk.StringVar()
minute.set("00")
hour=tk.StringVar()
hour.set("00")


def startCountdown():
    try:
        userinput = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        messagebox.showwarning('','Invalid input')

    while (userinput>-1):
            mins,secs=divmod(userinput,60)
            hours=0
            if mins>60:
                    hours,mins=divmod(userinput,60)


            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            window.update()
            time.sleep(1)

            if(userinput==0):
                os.system("taskkill /im python3.10.exe /f")
                

            userinput-=1   

hour_timer=tk.Entry(window,width=4,font=("Times","24"),textvariable=hour)
hour_timer.place(x=100,y=430)

minute_timer=tk.Entry(window,width=4,font=("Times","24"),textvariable=minute)
minute_timer.place(x=150,y=430)

seconds_timer=tk.Entry(window,width=4,font=("Times","24"),textvariable=second)
seconds_timer.place(x=200,y=430)


timer=startCountdown()





            
                    
    

    







window.mainloop()
