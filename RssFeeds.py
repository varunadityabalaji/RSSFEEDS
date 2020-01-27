# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:37:53 2020

@author: varun
"""

import feedparser
from tkinter import *
import tkinter as t

window = t.Tk()
window.title("NewsFeed")
canvas = t.Canvas(window,height=400,width=700)
canvas.pack()

frame = t.Frame(window, bg="white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)



content = t.Text(frame, bg="#ADD8E6", height=400, width=700)


NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
i=0

while i<len(NewsFeed.entries):
    content.insert(INSERT,NewsFeed.entries[i].published+"\n")    
    content.insert(INSERT,NewsFeed.entries[i].summary+"\n")
    content.insert(INSERT,NewsFeed.entries[i].link+"\n\n\n")
    i+=1

content.pack()
window.mainloop()

