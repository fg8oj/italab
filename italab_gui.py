#!/usr/bin/python3
import serial
import os
import tkinter
from tkinter import *


ser = serial.Serial('/dev/ttyUSB2', baudrate=57600,bytesize=serial.SEVENBITS)
ser.flushInput()
ser.flushOutput()

root = tkinter.Tk()
root.geometry("300x36+0+0")
root.configure(bg='green')
output_text = StringVar()
output_text.set("")
msg = Message(root,textvariable = output_text, font= ('Aerial Bold', 9),justify=CENTER,width=300,fg="white",bg="green")
msg.pack()
root.wm_attributes('-type', 'splash')
root.attributes('-topmost', True)

ligne=""
dirpower=0
refpower=0
swr=0
current=0
temperature=0
ptt=False
optt=True

def update():
  global dirpower,current,swr,temperature,ptt,optt,output_text,root,refpower
  if (ptt!=optt):
    optt=ptt
  os.system('clear')
  if (ptt==True):
    print("DIR\t",dirpower,"\nREF\t",refpower,"\nSWR\t",swr)
    root.configure(background='red')
    msg.configure(background='red')
    tm="ON AIR\t\t\tTemp.:\t" + str(temperature) + "°C\nPW: " + str(round((dirpower-refpower/1.2))) + "W\tCurrent: " + str(current) + "A\tS W R: " + str(swr)
  else:
    root.configure(background='green')
    msg.configure(background='green')
    tm="OFF AIR\t\t\tTemp.:\t" + str(temperature) + "°C"
  output_text.set(tm)
  root.update()

def check(ligne,valeur,multi):
   retour=""
   if (ligne.find(valeur)>=0):
     tm=ligne[ligne.find(valeur)+len(valeur):len(ligne)]
     #print(ligne,"\t",tm,"\t")
     tm=cleanstr(tm)
     tm=(tm*multi)
     if (tm!=None):
       if (tm!=dirpower):
         retour=tm
         return retour
     return 0

def cleanstr(val):
  nb=0
  for c in val:
    flag=True
    try:
      int(c)
    except ValueError:
        flag = False
        break
    if (flag==True):
      nb=nb+1
      continue
  #print("*\t",val,"\t",str(nb))
  val=val[0:nb] 
  val=int(val)
  if (val==None):
    val=0
  return val

while True:
 for line in ser.read():
  ligne=ligne+chr(line)
  if (ligne.find("p4.pic=39")>=0):
    ptt=True
    update()
  if (ligne.find("p4.pic=38")>=0):
    ptt=False
    update()

  if(ligne.find("add")>=0):
   tm=check(ligne,"j0.val=",8)
   if ( tm!=dirpower and tm!=0 and tm!=None):
       dirpower=tm
       update()
   tm=check(ligne,"j2.val=",1)
   if ( tm!=refpower and tm!=0 and tm!=None):
       refpower=tm
       update()
   tm=check(ligne,"x2.val=",0.01)
   if (tm!=temperature and tm!=0 and tm!=None):
       temperature=tm
       update()
   tm=check(ligne,"x0.val=",0.01)
   if (tm!=current and tm!=0 and tm!=None):
       current=tm
       update()
   tm=check(ligne,"x5.val=",0.01)
   if (tm!=swr and tm!=0 and tm!=None):
       swr=tm
       update()
   ligne=""

ser.close()


root.mainloop()
