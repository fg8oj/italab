import serial
import os

ser = serial.Serial('/dev/ttyUSB1', baudrate=57600,bytesize=serial.SEVENBITS)
ser.flushInput()
ser.flushOutput()

ligne=""
dirpower=0
swr=0
current=0
temperature=0
ptt=False
optt=True

def update():
  global dirpower,current,swr,temperature,ptt,optt
  if (ptt!=optt):
    optt=ptt
  os.system('clear')
  if (ptt==True):
    print("ON AIR\t\t\tTemp.:\t",str(temperature),"°C\nPW: ",str(round(dirpower/1.2)),"W","\t","Current: ",str(current),"A\t","S W R: ",str(swr))
  else:
    print("OFF AIR\t\t\tTemp.:\t",str(temperature),"°C")

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
  if(ligne.find("add")>=0):
   if (ligne.find("p4.pic=39")>=0):
    ptt=True
   if (ligne.find("p4.pic=38")>=0):
    ptt=False
   tm=check(ligne,"j0.val=",10)
   if ( tm!=dirpower and tm!=0 and tm!=None):
       dirpower=tm
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
