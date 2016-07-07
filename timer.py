#-________________________________-
import time
from Tkinter import *
from tkMessageBox import *


t=int(raw_input())
#Enter th amount of time
run=raw_input("Start?>")
mins=0
#only runs if the user types start
if run == "start":
   #loop while reaching t mins
   while mins!=t:
         print ">>>>>>>>>>>>>>>>>",mins
         #sleeps for half a min -___________-
         time.sleep(60)
         mins += 1
if mins==t:
   showinfo('Timer','TIME UP')     
