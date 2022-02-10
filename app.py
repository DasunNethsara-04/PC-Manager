from tkinter import *
from plyer import notification
import psutil
import os

btn_state = True

#functions
def cpucheck():
    cpu = psutil.cpu_percent()
    lbl1.config(text=str(cpu)+'%')
    lbl1.after(1000, cpucheck)

def ramcheck():
    per_ram = psutil.virtual_memory().percent
    lbl2.config(text=str(per_ram)+'%')
    lbl2.after(1000, ramcheck)

def totRam():
    total_ram = round((psutil.virtual_memory().total) / (1024 ** 3), 2)
    lbl3.config(text=str(total_ram)+'GB (usable)')
    lbl3.after(1000, totRam)

def aviRam():
    avil_ram = round((psutil.virtual_memory().available) / (1024 ** 3), 2)
    lbl4.config(text=str(avil_ram)+'GB')
    lbl4.after(1000, aviRam)

def useRam():
    used_ram = round((psutil.virtual_memory().used) / (1024 ** 3), 2)
    lbl5.config(text=str(used_ram)+'GB')
    lbl5.after(1000, useRam)

def freeRam():
    free_ram = round((psutil.virtual_memory().free) / (1024 ** 3), 2)
    lbl6.config(text=str(free_ram)+'GB')
    lbl6.after(1000, freeRam)

def btn():
    path = 'C:\\WINDOWS\\System32\\taskmgr.exe'
    os.startfile(os.path.join(path))

def active():
    global lbl3, lbl4, lbl5, lbl6
    frm = Frame(root, width=350, height=160, bg='#26242f', bd=0).place(x=0, y=121)
    Label(frm, text='Total RAM', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=110)
    Label(frm, text='Available RAM', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=140)
    Label(frm, text='Used RAM', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=170)
    Label(frm, text='Free RAM', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=200)
    lbl3 = Label(frm, font=('Calibri', 15, 'bold'), fg='green', bg='#26242f')
    lbl3.place(x=200, y=110)
    lbl4 = Label(frm, font=('Calibri', 15, 'bold'), fg='green', bg='#26242f')
    lbl4.place(x=200, y=140)
    lbl5 = Label(frm, font=('Calibri', 15, 'bold'), fg='green', bg='#26242f')
    lbl5.place(x=200, y=170)
    lbl6 = Label(frm, font=('Calibri', 15, 'bold'), fg='green', bg='#26242f')
    lbl6.place(x=200, y=200)

    Button(frm, text='Task Manager', font=('Calibri', 13), bd=0, bg='#bb3333', fg='white', command=btn).place(x=110, y=240)

def show():
    global lbl3, lbl4, lbl5, lbl6
    global btn_state
    if btn_state:
        active()
        totRam()
        aviRam()
        useRam()
        freeRam()
        btn_txt.set('↑')
        btn_state = False
    else:
        frm = Frame(root, width=350, height=160, bg='#26242f', bd=0).place(x=0, y=117)
        Label(frm, text='', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=110)
        Label(frm, text='', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=140)
        Label(frm, text='', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=170)
        Label(frm, text='', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=200)

        lbl3.config(text='')
        lbl4.config(text='')
        lbl5.config(text='')
        lbl6.config(text='')
        btn_txt.set('↓')
        btn_state = True



#main ui
root = Tk()
root.title('Techසර LK PC Manager')
root.geometry('350x280+570+350')
root.config(bg='#26242f')
root.iconbitmap('logo.ico')
root.resizable(0, 0)


'''notification.notify(
                app_name='PC Manager',
                title='Welcome to Techසර LK PC Manager!',
                message='We can help you to maintain your PC well.',
                app_icon='logo.ico',
                timeout=10,
                toast=False)'''

Label(root, text='PC Manager', font=('Calibri', 25), fg='white', bg='#26242f').pack()
#Label(root, text='+'*30, font=('Calibri', 25), fg='white', bg='#26242f').pack()

Label(root, text='CPU', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=50)
Label(root, text='RAM Per.', font=('Calibri', 15), fg='white', bg='#26242f').place(x=10, y=80)



lbl1 = Label(root, font=('Calibri', 15, 'bold'), fg='green', bg='#26242f')
lbl1.place(x=200, y=50)
lbl2 = Label(root, font=('Calibri', 15, 'bold'), fg='green', bg='#26242f')
lbl2.place(x=200, y=80)

btn_txt=StringVar()
btn_txt.set('↓')
Button(root, textvariable=btn_txt, bg='#26242f', fg='white', font=(15), bd=0, command=show).place(x=300, y=80)

cpucheck()
ramcheck()


root.mainloop()
