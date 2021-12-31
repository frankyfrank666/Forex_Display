from tkinter.constants import BOTTOM, TOP
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import Period
import matplotlib.pyplot as plt
import mplcursors
import datetime

def plot(SGDCNY,SGDMYR,SGDUSD,new_start,highlow,window, end = datetime.date.today()):
    plt.clf()

    new_start = Period.change_Time(new_start)
    
    fig, ((ax1), (ax2),(ax3)) = plt.subplots(3, 1)
    fig.set_size_inches(8, 8)
    
    if not highlow:
        ax1.plot(SGDCNY.loc[new_start:end].index, SGDCNY.loc[new_start:end]['High']/2+SGDCNY.loc[new_start:end]['Low']/2,'b' ,linewidth=1)
        ax2.plot(SGDMYR.loc[new_start:end].index, SGDMYR.loc[new_start:end]['High']/2+SGDMYR.loc[new_start:end]['Low']/2,'b' ,linewidth=1)
        ax3.plot(SGDUSD.loc[new_start:end].index, SGDUSD.loc[new_start:end]['High']/2+SGDUSD.loc[new_start:end]['Low']/2,'b' ,linewidth=1)
    else:
        ax1.plot(SGDCNY.loc[new_start:end].index, SGDCNY.loc[new_start:end]['Adj Close'],linewidth=1)
        ax1.plot(SGDCNY.loc[new_start:end].index, SGDCNY.loc[new_start:end]['High'],'g' ,linewidth=1)
        ax1.plot(SGDCNY.loc[new_start:end].index, SGDCNY.loc[new_start:end]['Low'],'r'  ,linewidth=1)

        ax2.plot(SGDMYR.loc[new_start:end].index, SGDMYR.loc[new_start:end]['Adj Close'],linewidth=1)
        ax2.plot(SGDMYR.loc[new_start:end].index, SGDMYR.loc[new_start:end]['High'],'g' ,linewidth=1)
        ax2.plot(SGDMYR.loc[new_start:end].index, SGDMYR.loc[new_start:end]['Low'],'r'  ,linewidth=1)

        ax3.plot(SGDUSD.loc[new_start:end].index, SGDUSD.loc[new_start:end]['Adj Close'],linewidth=1)
        ax3.plot(SGDUSD.loc[new_start:end].index, SGDUSD.loc[new_start:end]['High'],'g' ,linewidth=1)
        ax3.plot(SGDUSD.loc[new_start:end].index, SGDUSD.loc[new_start:end]['Low'],'r'  ,linewidth=1)

    ax1.yaxis.set_major_locator(plt.MultipleLocator(0.05))
    ax2.yaxis.set_major_locator(plt.MultipleLocator(0.02))
    ax3.yaxis.set_major_locator(plt.MultipleLocator(0.02))
    ax1.tick_params(labelright=True)
    ax2.tick_params(labelright=True)
    ax3.tick_params(labelright=True)

    ax1.set_ylabel('SGD-CNY\n'+str(round(SGDCNY['Adj Close'].iloc[-1],3)),rotation = 0)
    ax2.set_ylabel('SGD-MYR\n'+str(round(SGDMYR['Adj Close'].iloc[-1],3)),rotation = 0)
    ax3.set_ylabel('USD-SGD\n'+str(round(SGDUSD['Adj Close'].iloc[-1],3)),rotation = 0)
    ax1.grid('both')
    ax2.grid('both')
    ax3.grid('both')

    ax1.yaxis.set_label_coords(-0.13, 0.25)
    ax2.yaxis.set_label_coords(-0.13, 0.25)
    ax3.yaxis.set_label_coords(-0.13, 0.25)
    plt.subplots_adjust(left=0.15,right = 0.9,top=0.95,bottom=0.15)

    # canvas = FigureCanvasTkAgg(fig, master = window)  
    # toolbar = NavigationToolbar2Tk(canvas, window)

    # canvas.draw()
    # canvas.get_tk_widget().place(x=0, y=80)
    # toolbar.place(x=0, y=40)

    mplcursors.cursor(hover=True) 

    plt.show()

    return fig, ax1, ax2, ax3