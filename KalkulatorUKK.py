from tkinter import *
import tkinter.messagebox
import math


root = Tk()
root.geometry("650x400+300+300")
root.title("Kalkulator by Ikhsan Asagaf")

switch = None

# Button on press

def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def btntambah_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')


def btnkurang_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')


def btnkali_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')


def btnbagi_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnreset_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')


def btnpangkat_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')


def btnakar_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Terjadi Kesalahan!", "Cek Kembali Bilangan dan Operator Bilangan")


def titik_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')


def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def bukakurung_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')


def tutupkurung_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')


def hapus_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def btnsamadengan_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Terjadi Kesalahan!", "Cek Kembali Bilangan dan Operator Bilangan")


# Label



disp = Entry(root, font="Consolas 30", fg="black", bg="#b0cbf7", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
disp.bind("<Return>", btnsamadengan_clicked)
disp.bind("<Escape>", btnreset_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 Buttons

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

pi_btn = Button(btnrow1, text="  π ", font="Segoe 18", relief=GROOVE, bd=0, command=pi_clicked, fg="white", bg="#333333")
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Segoe 23", relief=GROOVE, bd=0, command=btn1_clicked, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Segoe 23", relief=GROOVE, bd=0,  command=btn2_clicked, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Segoe 23", relief=GROOVE, bd=0, command=btn3_clicked, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btntambah = Button(btnrow1, text="+", font="Segoe 23", relief=GROOVE, bd=0, command=btntambah_clicked, fg="white", bg="#333333")
btntambah.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

akar_btn = Button(btnrow2, text=" √x ", font="Segoe 18", relief=GROOVE, bd=0, command=btnakar_clicked, fg="white", bg="#333333")
akar_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow2, text="4", font="Segoe 23", relief=GROOVE, bd=0, command=btn4_clicked, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Segoe 23", relief=GROOVE, bd=0, command=btn5_clicked, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Segoe 23", relief=GROOVE, bd=0, command=btn6_clicked, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnkurang = Button(btnrow2, text="-", font="Segoe 23", relief=GROOVE, bd=0, command=btnkurang_clicked, fg="white", bg="#333333")
btnkurang.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

pangkat_btn = Button(btnrow3, text="x^y", font="Segoe 17", relief=GROOVE, bd=0, command=btnpangkat_clicked, fg="white", bg="#333333")
pangkat_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Segoe 23", relief=GROOVE, bd=0, command=btn7_clicked, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Segoe 23", relief=GROOVE, bd=0, command=btn8_clicked, fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Segoe 23", relief=GROOVE, bd=0, command=btn9_clicked, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnkali = Button(btnrow3, text="*", font="Segoe 23", relief=GROOVE, bd=0, command=btnkali_clicked, fg="white", bg="#333333")
btnkali.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

bukakurung_btn = Button(btnrow4, text="( ", font="Segoe 21", relief=GROOVE, bd=0, command=bukakurung_clicked, fg="white", bg="#333333")
bukakurung_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tutupkurung_btn = Button(btnrow4, text=")", font="Segoe 21", relief=GROOVE, bd=0, command=tutupkurung_clicked, fg="white", bg="#333333")
tutupkurung_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 23", relief=GROOVE, bd=0, command=btn0_clicked, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnbagi = Button(btnrow4, text="/", font="Segoe 23", relief=GROOVE, bd=0, command=btnbagi_clicked, fg="white", bg="#333333")
btnbagi.pack(side=LEFT, expand=TRUE, fill=BOTH)
# Row 5 Buttons

btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH)

titik_btn = Button(btnrow5, text="•", font="Segoe 21", relief=GROOVE, bd=0, command=titik_clicked, fg="white", bg="#333333")
titik_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

hapus_btn = Button(btnrow5, text="⌫", font="Segoe 20", relief=GROOVE, bd=0, command=hapus_clicked, fg="white", bg="#333333")
hapus_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnreset = Button(btnrow5, text="C", font="Segoe 23", relief=GROOVE, bd=0, command=btnreset_clicked, fg="white", bg="#333333")
btnreset.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnsamadengan = Button(btnrow5, text="=", font="Segoe 23", relief=GROOVE, bd=0, command=btnsamadengan_clicked, fg="white", bg="#333333")
btnsamadengan.pack(side=LEFT, expand=TRUE, fill=BOTH)

root.mainloop()