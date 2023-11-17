from customtkinter import *
from bkendsqlite import *
from PIL import Image
import time
from CTkTable import *
from random import *


"""__________________________________________________________________________________________________________"""

ft = "candara"
p = ["img n.png","img1.png","img2.png","img3.png"]
pn=p[0]
set_appearance_mode("dark")
pv = ["Never spend money before you have it.","Spending is quick; earning is slow.","Creditors have better memories than debtors.","A penny saved is a penny earned."]
"""__________________________________________________________________________________________________________"""
#for changing theme
def chtheme():
    v = bt.get()
    if v:
        set_appearance_mode("light")
    else:
        set_appearance_mode("dark")

# for showing time
def shtime():
    tt = time.strftime("Time : %I:%M:%S %p ")
    lt.configure(text=tt)
    lt.after(1000, shtime)


c = 0

# register transactions
def Swin1():
    global c

    def exit():
        global c
        c = 0
        win.destroy()

    def getval():
        global c
        name = e1.get()
        amt = e2.get()
        if amt.isdigit() != True:
            l.configure(text="Wrong value enter again")
            e2.delete(0, END)
        else:
            l.configure(text="")
            a = insval(name, int(amt), ot.get())
            c += 1
            if a == 1:
                e1.delete(0, END)
                e2.delete(0, END)
                l3.configure(text=f"Current Record entered : {c}")
                bb.configure(text=f"Balance amount : ${binfo()[1]}")
                bu.configure(text=f"Used amount :     ${binfo()[0]}")

    ty = ["Debit", "Credit"]

    win = CTkFrame(mainwin, fg_color=("#FFFFFF", "#000"), height=360, width=640)
    win.place(x=0, y=0,)

    ph3 = CTkImage(light_image=Image.open("img\\back.png"), dark_image=Image.open("img\\back.png"), size=(40, 40))
    i3 = CTkButton(win, image=ph3, bg_color=("#FFFFFF", "#000"), text="", hover=False, fg_color=("#FFFFFF", "#000"),
                   command=exit)
    i3.place(x=-20, y=10)

    ltt = CTkLabel(win, text="Register Transaction", font=(ft, 22, "bold"), bg_color=("#FFFFFF", "#000"))
    ltt.place(x=110, y=23)

    l = CTkLabel(win, text="", font=("MV boli", 10), bg_color=("#FFFFFF", "#000"))
    l.place(x=320, y=190)

    l1 = CTkLabel(win, fg_color=("#FFFFFF", "#000"), font=(ft, 24, "bold"), text="Transaction Name",
                  text_color="#1E90FF", bg_color=("#FFFFFF", "#000"))
    l1.place(x=80, y=120)
    l2 = CTkLabel(win, fg_color=("#FFFFFF", "#000"), font=(ft, 24, "bold"), text="Transaction Amount",
                  text_color="#1E90FF", bg_color=("#FFFFFF", "#000"))
    l2.place(x=80, y=160)

    l3 = CTkLabel(win, text=f"Current Record entered : {c}", font=(ft, 18,"bold"), bg_color=("#FFFFFF", "#000"))
    l3.place(x=400, y=300)

    namevar = StringVar()
    amtvar = StringVar()
    e1 = CTkEntry(win, width=180, textvariable=namevar, font=("microsoft yahei ui", 15), border_color="#1E90FF")
    e2 = CTkEntry(win, width=180, textvariable=amtvar, font=("microsoft yahei ui", 15), border_color="#1E90FF")
    e1.place(x=320, y=125)
    e2.place(x=320, y=165)

    b1 = CTkButton(win, bg_color=("#FFFFFF", "#000"), text="SUBMIT", fg_color="#7CFC00", text_color="#000",
                   font=(ft, 18, "bold"), corner_radius=12, border_spacing=7, command=getval)
    b1.place(x=120, y=240)

    typ = StringVar()
    ot = CTkOptionMenu(win, width=30, height=27, button_color="#1E90FF", hover=False,
                       values=ty, variable=typ, bg_color=("#FFFFFF", "#000"), font=(ft, 18, "bold"))
    ot.set("Debit")
    ot.place(x=400, y=50)

    bu = CTkLabel(win, text=f"Used amount :     ${binfo()[0]}",bg_color=("#FFFFFF", "#000"),
                  fg_color=("#FFFFFF", "#000"),font=(ft,18,"bold"))
    bu.place(x=400,y=240)
    bb = CTkLabel(win, text=f"Balance amount : ${binfo()[1]}", bg_color=("#FFFFFF", "#000"),
                   fg_color=("#FFFFFF", "#000"),font=(ft, 18, "bold"))
    bb.place(x=400, y=270)

# monthly record
def Swin2():
    mon = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December"]

    def intb():
        tb.configure(rows=len(valtb(mon.index(om.get()) + 1, ot.get()) + [None]))
        tb.configure(values=[(1, 1)] + valtb(mon.index(om.get()) + 1, ot.get()))
        tb.insert(0, 0, value="Transaction name")
        tb.insert(0, 1, value="Transaction amt")

    win = CTkFrame(mainwin, width=640, height=360, fg_color=("#FFFFFF", "#000"), bg_color=("#FFFFFF", "#000"))
    win.place(x=0, y=0)
    sf = CTkScrollableFrame(win, width=360, height=220, bg_color=("#FFFFFF", "#000"), fg_color=("#FFFFFF", "#000"))
    sf.place(x=40, y=60)

    ph3 = CTkImage(light_image=Image.open("img\\back.png"), dark_image=Image.open("img\\back.png"), size=(40, 40))
    i3 = CTkButton(win, image=ph3, bg_color=("#FFFFFF", "#000"), text="", hover=False, fg_color=("#FFFFFF", "#000"),
                   command=win.destroy)
    i3.place(x=-20, y=10)

    ltt = CTkLabel(win, text="Monthly Records", font=(ft, 22, "bold"), bg_color=("#FFFFFF", "#000"))
    ltt.place(x=110, y=23)

    m = StringVar()
    om = CTkOptionMenu(win, width=30, height=27, button_color="#1E90FF", hover=False,
                       values=mon, variable=m, bg_color=("#FFFFFF", "#000"), font=(ft, 18, "bold"))
    om.set(f"{mon[d.month-1]}")
    om.place(x=450, y=70)


    ty = ["Credit", "Debit"]
    typ = StringVar()
    ot = CTkOptionMenu(win, width=30, height=27, button_color="#1E90FF", hover=False,
                       values=ty, variable=typ, bg_color=("#FFFFFF", "#000"), font=(ft, 18, "bold"))
    ot.set("Debit")
    ot.place(x=450, y=120)

    tb = CTkTable(sf, row=2, column=2, header_color="#1E90FF", corner_radius=7, values=[[1, 1]])
    tb.pack(padx=8, pady=8)
    tb.insert(0, 0, value="Transaction name")
    tb.insert(0, 1, value="Transaction amt")

    b1 = CTkButton(win, bg_color=("#FFFFFF", "#000"), text="SHOW", fg_color="#7CFC00", text_color="#000",
                   font=(ft, 18, "bold"), corner_radius=12, border_spacing=7, command=intb)
    b1.place(x=450, y=250)

    lp = CTkLabel(win,fg_color=("#FFFFFF", "#000"),text=f"{pv[randint(0,3)]}",font=("mv boli",14,"bold"))
    lp.place(x=80,y=300)

# search records
def Swin3():
    def intb():
        tb.configure(rows=len(shtabels(e2.get(), ot.get())) + 1)
        tb.configure(values=[(1, 1)] + shtabels(e2.get(), ot.get()))
        tb.insert(0, 0, value="Trans. Name")
        tb.insert(0, 1, value="Trans. Amt")
        tb.insert(0, 2, value="Trans. Date")
        e2.delete(0, END)

    win = CTkFrame(mainwin, width=640, height=360, fg_color=("#FFFFFF", "#000"), bg_color=("#FFFFFF", "#000"))
    win.place(x=0, y=0)

    ph3 = CTkImage(light_image=Image.open("img\\back.png"), dark_image=Image.open("img\\back.png"), size=(40, 40))
    i3 = CTkButton(win, image=ph3, bg_color=("#FFFFFF", "#000"), text="", hover=False, fg_color=("#FFFFFF", "#000"),
                   command=win.destroy)
    i3.place(x=-20, y=10)

    ltt = CTkLabel(win, text="Search Transaction", font=(ft, 22, "bold"), bg_color=("#FFFFFF", "#000"))
    ltt.place(x=110, y=23)

    dvar = StringVar()
    e2 = CTkEntry(win, width=180, textvariable=dvar, font=("microsoft yahei ui", 13), border_color="#1E90FF")
    e2.place(x=430, y=190)
    
    l2 = CTkLabel(win, fg_color=("#FFFFFF", "#000"), font=(ft, 16, "bold"), text="Transaction Date",
                  bg_color=("#FFFFFF", "#000"))
    l2.place(x=430, y=160)

    l = CTkLabel(win, text="Kindly enter date(YYYY-MM-DD) like this", font=("MV boli", 10),
                 bg_color=("#FFFFFF", "#000"))
    l.place(x=425, y=220)

    ty = ["Credit", "Debit"]
    typ = StringVar()
    ot = CTkOptionMenu(win, width=30, height=27, button_color="#1E90FF", hover=False,
                       values=ty, variable=typ, bg_color=("#FFFFFF", "#000"), font=(ft, 18, "bold"))
    ot.set("Debit")
    ot.place(x=430, y=70)
    sf = CTkScrollableFrame(win, width=360, height=280, bg_color=("#FFFFFF", "#000"), fg_color=("#FFFFFF", "#000"))
    sf.place(x=40, y=60)

    tb = CTkTable(sf, row=2, column=3, header_color="#1E90FF", corner_radius=7, values=[[1, 1, 1]])
    tb.pack(padx=8, pady=8)
    tb.insert(0, 0, value="Trans. Name")
    tb.insert(0, 1, value="Trans. Amt")
    tb.insert(0, 2, value="Trans. Date")

    b1 = CTkButton(win, bg_color=("#FFFFFF", "#000"), text="Search", fg_color="#7CFC00", text_color="#000",
                   font=(ft, 18, "bold"), corner_radius=12, border_spacing=7, command=intb)
    b1.place(x=430, y=280)

# Transaction report
def Swin4():
    def up():
        mn = om.get()
        l1.configure(text=f"Total no of Transaction : {info(mn)[0]}")
        l2.configure(text=f"Total amount Spended : {info(mn)[1]}")
        l3.configure(text=f"Total amount received : {info(mn)[7]}")
        l4.configure(text=f"Avg amount Spended : {info(mn)[4]}")
        l5.configure(text=f"Avg amount Recived : {info(mn)[9]}")
        l6.configure(text=f"Balance amount in account : {info(mn)[-1]}")
        l7.configure(text=f"Max amount spended in month : {info(mn)[5]}")
        l8.configure(text=f"Min amount spended in month : {info(mn)[6]}")
        l9.configure(text=f"Max amount received in month : {info(mn)[11]}")
        l10.configure(text=f"Min amount received in month : {info(mn)[12]}")


    mon = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December"]
    win = CTkFrame(mainwin, width=640, height=360, fg_color=("#FFFFFF", "#000"), bg_color=("#FFFFFF", "#000"))
    win.place(x=0, y=0)

    ph3 = CTkImage(light_image=Image.open("img\\back.png"), dark_image=Image.open("img\\back.png"), size=(40, 40))
    i3 = CTkButton(win, image=ph3, bg_color=("#FFFFFF", "#000"), text="", hover=False, fg_color=("#FFFFFF", "#000"),
                   command=win.destroy)
    i3.place(x=-20, y=10)

    ltt = CTkLabel(win, text="Transaction Report", font=(ft, 22, "bold"), bg_color=("#FFFFFF", "#000"))
    ltt.place(x=110, y=23)

    sf = CTkScrollableFrame(win, width=560, height=260, bg_color=("#FFFFFF", "#000"), fg_color="#FFF",border_width=2,border_color="#000")
    sf.place(x=30, y=70)

    l1 = CTkLabel(sf, text=f"Total no of Transaction : {tno}",text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l1.pack(padx=5, pady=5, side='top',anchor = W)

    l2 = CTkLabel(sf, text=f"Total amount Spended : {tot}", text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l2.pack(padx=5, pady=5, side='top',anchor = W)

    l3= CTkLabel(sf, text=f"Total amount received : {dtot}", text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l3.pack(padx=5, pady=5, side='top',anchor = W)

    l4 = CTkLabel(sf, text=f"Avg amount Spended : {avg}", text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l4.pack(padx=5, pady=5, side='top',anchor = W)

    l5 = CTkLabel(sf, text=f"Avg amount Recived : {davg}", text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l5.pack(padx=5, pady=5, side='top',anchor = W)
    l6 = CTkLabel(sf, text=f"Balance amount in account : {ab}", text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l6.pack(padx=5, pady=5, side='top', anchor=W)

    ph4 = CTkImage(light_image=Image.open("img\\img r.png"), dark_image=Image.open("img\\img r.png"), size=(30, 30))
    i4 = CTkButton(win, image=ph4, bg_color=("#FFFFFF", "#000"), text="", hover=False, fg_color=("#FFFFFF", "#000"),
                   command=up)
    i4.place(x=520, y=25)

    m = StringVar()
    om = CTkOptionMenu(win, width=30, height=27, button_color="#1E90FF", hover=False,
                       values=mon, variable=m, bg_color=("#FFFFFF", "#000"), font=(ft, 18, "bold"))
    om.set(f"{mon[d.month-1]}")
    om.place(x=450,y=30)

    l7 = CTkLabel(sf, text=f"Max amount spended in this month : {mxm}", text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l7.pack(padx=5, pady=5, side='top', anchor=W)

    l8 = CTkLabel(sf, text=f"Min amount spended in this month : {mnm}", text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l8.pack(padx=5, pady=5, side='top', anchor=W)

    l9 = CTkLabel(sf, text=f"Max amount received in this month : {dmxm}", text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l9.pack(padx=5, pady=5, side='top', anchor=W)

    l10 = CTkLabel(sf, text=f"Min amount received in this month : {dmnm}", text_color="#000",
                  bg_color="#FFF", font=(ft, 16, "bold"))
    l10.pack(padx=5, pady=5, side='top', anchor=W)

    l11 = CTkLabel(win,text=f"Report from {sd} to {D}", text_color="#000",
                  bg_color="#FFF", font=(ft, 12, "bold"))
    l11.place(x=360,y=80)

    l12 = CTkLabel(win, text=f"Report according to above selected month", text_color="#000",
                  bg_color="#FFF", font=(ft, 12, "bold"))
    l12.place(x=360, y=100)



"""_________________________________________________________________________________________________________________"""

# Mainwindow
mainwin = CTk()
mainwin.geometry("640x360+0+0")
mainwin.resizable(False, False)
mainwin.title("Financial_assistance")

mainwin.iconbitmap("img\\ic.ico")

f = CTkFrame(mainwin, fg_color=("#FFFFFF", "#000"), height=360, width=640)
f.place(x=0, y=0)


ph = CTkImage(light_image=Image.open(f"img\{pn}"), dark_image=Image.open(f"img\{pn}"), size=(350, 300))
i = CTkLabel(mainwin, text="", image=ph, bg_color=("#FFFFFF", "#000"))
i.place(x=250, y=50)

ph2 = CTkImage(light_image=Image.open("img\\moon.png"), dark_image=Image.open("img\\sun.png"), size=(30, 30))
i2 = CTkLabel(mainwin, text="", image=ph2, bg_color=("#FFFFFF", "#000"))
i2.place(x=360, y=28)

ph3 = CTkImage(light_image=Image.open("img\\back.png"), dark_image=Image.open("img\\back.png"), size=(40, 40))
i3 = CTkButton(mainwin, image=ph3, bg_color=("#FFFFFF", "#000"), text="", hover=False, fg_color=("#FFFFFF", "#000"),
               command=mainwin.destroy)
i3.place(x=-20, y=10)

ld = CTkLabel(mainwin, text=f"Date : {D}", bg_color=("#FFFFFF", "#000"), font=("candara", 14, "bold"))
ld.place(x=500, y=10)
lt = CTkLabel(mainwin, bg_color=("#FFFFFF", "#000"), font=("candara", 14, "bold"))
lt.place(x=500, y=30)

shtime()

l1 = CTkLabel(mainwin, text="Financial assistance", font=(ft, 22, "bold"), bg_color=("#FFFFFF", "#000"))
l1.place(x=110, y=23)

l2 = CTkLabel(mainwin, text="creted by Mukesh", font=("MV Boli", 8), bg_color=("#FFFFFF", "#000"))
l2.place(x=550, y=320)

b1 = CTkButton(mainwin, text="Register transaction", font=(ft, 18, "bold"), border_spacing=6,
               fg_color="#1E90FF", corner_radius=12, bg_color=("#FFFFFF", "#000"), command=Swin1)
b1.place(x=40, y=90)

b2 = CTkButton(mainwin, text="Monthly Records", font=(ft, 18, "bold"), border_spacing=6,
               fg_color="#1E90FF", corner_radius=12, bg_color=("#FFFFFF", "#000"), command=Swin2)
b2.place(x=40, y=140)

b3 = CTkButton(mainwin, text="Transaction Report", font=(ft, 18, "bold"), border_spacing=6,
               fg_color="#1E90FF", corner_radius=12, bg_color=("#FFFFFF", "#000"), command=Swin4)
b3.place(x=40, y=240)

b4 = CTkButton(mainwin, text="Search Transaction", font=(ft, 18, "bold"), border_spacing=6,
               fg_color="#1E90FF", corner_radius=12, bg_color=("#FFFFFF", "#000"), command=Swin3)
b4.place(x=40, y=190)

bt = CTkSwitch(mainwin, command=chtheme, text="", onvalue=1, offvalue=0, bg_color=("#FFFFFF", "#000"))
bt.place(x=400, y=30)

mainwin.mainloop()
conn.close()
