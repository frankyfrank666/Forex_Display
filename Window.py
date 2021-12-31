import get_Data
from tkinter import *
from Plot import *

[SGDCNY,SGDMYR,SGDUSD] = get_Data.get_Data()

window = Tk()
window.title('FOREX Rate')
ws = str(int(window.winfo_screenwidth()/2)) # width of the screen
hs = str(window.winfo_screenheight()) # height of the screen
window.geometry(ws+'x'+hs+'+'+ws+'+'+'0')

highlow = 0
current = 'MX'
def change_view():
    global highlow
    global current

    highlow = not highlow
    if highlow == 1:
        High_Low['text'] = "View Medium"
    else:
        High_Low['text'] = "View\nHigh-Low"
    
    plot(SGDCNY,SGDMYR,SGDUSD,current,highlow,window)


def plt1():
    global current
    current = 'MX'
    plot(SGDCNY,SGDMYR,SGDUSD,'MX',highlow,window)
def plt2():
    global current
    current = '1Y'
    plot(SGDCNY,SGDMYR,SGDUSD,'1Y',highlow,window)
def plt3():
    global current
    current = '6M'
    plot(SGDCNY,SGDMYR,SGDUSD,'6M',highlow,window)
def plt4():
    global current
    current = '1M'
    plot(SGDCNY,SGDMYR,SGDUSD,'1M',highlow,window)
def plt5():
    global current
    current = '2W'
    plot(SGDCNY,SGDMYR,SGDUSD,'2W',highlow,window)

Max = Button(master = window,
                     height = 2,
                     width = 10,
                     text = "Max",command = plt1 )
One_Year = Button(master = window,
                     height = 2,
                     width = 10,
                     text = "1 Year",command = plt2)
Six_Month = Button(master = window,
                     height = 2,
                     width = 10,
                     text = "6 Month",command = plt3)
One_Month = Button(master = window,
                     height = 2,
                     width = 10,
                     text = "1 Month",command = plt4)
Two_Week = Button(master = window,
                     height = 2,
                     width = 10,
                     text = "2 Weeks",command = plt5)
High_Low = Button(master = window,
                     height = 2,
                     width = 10,
                     text = "View High-Low" , command = change_view)

Max.place(x=0, y=0)
One_Year.place(x=110, y=0)
Six_Month.place(x=220, y=0)
One_Month.place(x=330, y=0)
Two_Week.place(x=440, y=0)
High_Low.place(x=560, y=0)

plt3()
window.mainloop()