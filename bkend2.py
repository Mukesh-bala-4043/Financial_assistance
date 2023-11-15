import datetime as dt
import sqlite3
from CTkMessagebox import *

conn = sqlite3.connect("Financial_assistance.db")
cr = conn.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS Credit (tname TEXT,tamt REAL,tdate TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS Debit (tname TEXT,tamt REAL,tdate TEXT)")

d = dt.datetime.now()
D = f"{d.year}-{d.month}-{d.day}"
try:
    cr = conn.cursor()
    cr.execute("select * from Debit")
    sd = cr.fetchall()[0][2]
    cr.close()
except:
    sd = D


def insval(name, amt,tb):
    cr =conn.cursor()
    cr.execute(f"INSERT INTO {tb}(tname, tamt, tdate) VALUES (?, ?, ?)", (name, amt, D))
    conn.commit()

    if cr.rowcount == 1:
        mb = CTkMessagebox(
            title="Success",
            message="Transaction saved successfully.",
            icon="check",
            button_hover_color="#7CFC00",
            cancel_button="circle",
            button_color="#7CFC00",
            cancel_button_color="#FF0000",
            button_text_color="#000"
        )
        if mb.get() == "ok":
            mb.destroy()
            cr.close()
        return 1

def info(m):
    global tno, tot, maxamt, minamt, avg, mxm, mnm, dtot, dmaxamt, dminamt, davg, dmxm, dmnm, dtno, ab
    cr =conn.cursor()
    mon = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December"]
    mn = mon.index(m)+1
    try:
        cr.execute(f"select max(tamt) from Credit where tdate like '____-{mn}-%'")
        maxamt = cr.fetchall()[0][0]
        cr.execute(f"select avg(tamt) from Credit where tdate like '____-{mn}-%'")
        avg = cr.fetchall()[0][0]
        cr.execute(f"select sum(tamt) from Credit where tdate like '____-{mn}-%'")
        tot = cr.fetchall()[0][0]
        cr.execute(f"select count(*) from Credit where tdate like '____-{mn}-%'")
        tno = cr.fetchall()[0][0]
        cr.execute(f"select min(tamt) from Credit where tdate like '____-{mn}-%'")
        minamt = cr.fetchall()[0][0]
        cr.execute("select  strftime('%m', tdate) from Credit where tamt = ? ", (maxamt,))
        mxmonth = cr.fetchall()[0]
        cr.execute("select  strftime('%m', tdate) from Credit where tamt = ? ", (minamt,))
        mnmonth = cr.fetchall()[0]
        mnm = mon[int(mnmonth[0]) - 1]
        mxm = mon[int(mxmonth[0]) - 1]

        cr.execute(f"select max(tamt) from Debit where tdate like '____-{mn}-%'")
        dmaxamt = cr.fetchall()[0][0]
        cr.execute(f"select avg(tamt) from Debit where tdate like '____-{mn}-%'")
        davg = cr.fetchall()[0][0]
        cr.execute(f"select sum(tamt) from Debit where tdate like '____-{mn}-%'")
        dtot = cr.fetchall()[0][0]
        cr.execute(f"select count(*) from Debit where tdate like '____-{mn}-%'")
        dtno = cr.fetchall()[0][0]
        cr.execute(f"select min(tamt) from Debit where tdate like '____-{mn}-%'")
        dminamt = cr.fetchall()[0][0]
        cr.execute("select  strftime('%m', tdate) from Debit where tamt = ? ", (dmaxamt,))
        mxmonth = cr.fetchall()[0]
        cr.execute("select  strftime('%m', tdate) from Debit where tamt = ? ", (dminamt,))
        mnmonth = cr.fetchall()[0]
        dmnm = mon[int(mnmonth[0]) - 1]
        dmxm = mon[int(mxmonth[0]) - 1]
        tno += dtno
        ab = dtot - tot
        cr.close()
    except:
        cr.close()
        return (None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)
    return (tno, tot, maxamt, minamt, avg, mxm, mnm, dtot, dmaxamt, dminamt, davg, dmxm, dmnm, dtno, ab)
#          (0    1    2       3         4   5     6     7      8        9         10    11     12     13    14)


tno = None
tot = None
maxamt = None
minamt = None
avg = None
mxm = None
mnm = None
dtno = None
dtot = None
dmaxamt = None
dminamt = None
davg = None
dmxm = None
dmnm = None
ab = None

def valtb(mon,tb):
    cr = conn.cursor()
    cr.execute(f"select tname,sum(tamt) from {tb} where tdate like '____-{str(mon)}%'  group by tname;")
    a = cr.fetchall()
    cr.close()
    return a
def shtabels(tt,tb):

    cr = conn.cursor()
    cr.execute(f"select tname,tamt,tdate from {tb} where tdate = ? ",(tt,))
    v = cr.fetchall()
    cr.close()
    return v

def chs():
    cr = conn.cursor()
    cr.execute(f"select tdate from Credit where tdate like '____-{str(d.month-1)}-%'")
    p = cr.fetchall()
    cr.execute(f"select tdate from Credit where tdate like '____-{str(d.month)}-%'")
    f = cr.fetchall()
    if p != [] and f != []:
        return 0
    else:
        return 1
def suggest():
    cr = conn.cursor()