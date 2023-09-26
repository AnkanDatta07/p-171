# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:19:23 2023

@author: Ankan Datta
"""

from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.title("TimeZone")
root.geometry("1000x900")
india_image = ImageTk.PhotoImage(Image.open("india.jpg"))

#------------------India-------------------

india_label = Label(root, text = "India")
india_label.place(relx = 0.2, rely = 0.05, anchor = CENTER)

india_clock = Label(root)
india_clock['image'] = india_image
india_clock.place(relx = 0.2, rely = 0.35, anchor = CENTER)

india_time = Label(root)
india_time.place(relx = 0.2, rely = 0.69, anchor = CENTER)

#------------------USA---------------------

usa_label = Label(root, text = "USA")
usa_label.place(relx = 0.8, rely = 0.05, anchor = CENTER)

usa_clock = Label(root)
usa_clock['image'] = clock_image
usa_clock.place(relx = 0.8, rely = 0.35, anchor = CENTER)

usa_time = Label(root)
usa_time.place(relx = 0.8, rely = 0.69, anchor = CENTER)

#------------------Australia---------------------

aus_label = Label(root, text = "Australia")
aus_label.place(relx = 0.2, rely = 0.5, anchor = CENTER)

aus_clock = Label(root)
aus_clock['image'] = clock_image
aus_clock.place(relx = 0.2, rely = 0.75, anchor = CENTER)

aus_time = Label(root)
aus_time.place(relx = 0.2, rely = 0.69, anchor = CENTER)

#------------------Japan---------------------

jap_label = Label(root, text = "USA")
usa_label.place(relx = 0.8, rely = 0.5, anchor = CENTER)

jap_clock = Label(root)
jap_clock['image'] = clock_image
jap_clock.place(relx = 0.8, rely = 0.35, anchor = CENTER)

jap_time = Label(root)
jap_time.place(relx = 0.8, rely = 0.69, anchor = CENTER)

class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        india_time['text'] = "Time - " + current_time
        india_time.after(200, self.times)
        
class USA():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        usa_time['text'] = "Time - " + current_time
        usa_time.after(200, self.times)
  
obj_of_india = India()
obj_of_usa = USA()

btn1 = Button(root, text = "Show Time", command=obj_of_india.times)
btn1.place(relx = 0.2, rely = 0.8, anchor = CENTER)

btn2 = Button(root, text = "Show Time", command = obj_of_usa.times)
btn2.place(relx = 0.75, rely = 0.8)


root.mainloop()