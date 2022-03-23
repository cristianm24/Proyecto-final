#importar librerias
from tkinter import *
import time
from playsound import playsound


#Display 
vent = Tk()
vent.geometry('400x300')
vent.resizable(0,0)
vent.config(bg ='blanched almond')
vent.title('Proyecto Final-Hora actual y Temprizador')
Label(vent, text = 'Temporizador y Hora Actual' , font = 'arial 20 bold',  bg ='papaya whip').pack()


#display hora actual

Label(vent, font ='arial 15 bold', text = 'Hora actual:', bg = 'papaya whip').place(x = 40 ,y = 70)


#Funcion de la hora actual + display
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)

curr_time =Label(vent, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(x = 190 , y = 70)
clock()


#Funcion para temporizador

#Funcion y widget para variables

# segundos
seg = StringVar()
Entry(vent, textvariable = seg, width = 2, font = 'arial 12').place(x=250, y=155)
seg.set('00')

# minutos
mtos= StringVar()
Entry(vent, textvariable = mtos, width =2, font = 'arial 12').place(x=225, y=155)
mtos.set('00')


# horas
hrs= StringVar()
Entry(vent, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=155)
hrs.set('00')

#funcion para iniciar el temporizador

def countdown():
    tiempo = int(hrs.get())*3600+ int(mtos.get())*60 + int(seg.get())
    while tiempo > -1:
        minutos,segundos = (tiempo // 60 , tiempo % 60)
        
        hora = 0
        if minutos > 60:
            hora , minutos = (minutos // 60 , minutos % 60)
            
        seg.set(segundos)
        mtos.set(minutos)
        hrs.set(hora)
        
        vent.update()
        time.sleep(1)

        if(tiempo == 0):
            playsound("Loud_Alarm_Clock_Buzzer.mp3")
            seg.set('00')
            mtos.set('00')
            hrs.set('00')
        tiempo -= 1

Label(vent, font ='arial 15 bold', text = 'set the time',   bg ='papaya whip').place(x = 40 ,y = 150)

Button(vent, text='START', bd ='5', command = countdown, bg = 'antique white', font = 'arial 10 bold').place(x=150, y=210)
        


vent.mainloop() 
