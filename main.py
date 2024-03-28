from tkinter import Tk, Entry, Button, Label
from numpy import corrcoef

def std_dev(*args):
    n = len(args[0])
    lst = [int (i) for i in args[0]]
    ave = sum(lst)/n
    std = 0
    for i in lst:
        std += (i - ave)**2
    return (std/(n - 1))**0.5

StatisticalCalculator = Tk()
StatisticalCalculator.minsize(500,380)
StatisticalCalculator.columnconfigure(index=1,weight=1)
StatisticalCalculator.rowconfigure(index=3,weight=1)
StdDev = Button(StatisticalCalculator, text='Standard square deviation')
StdDev.grid(row=0,column=0, padx=11, pady=5)
Corel = Button(StatisticalCalculator, text='Corel')
Corel.grid(row=1,column=0, padx=11, pady=5, sticky='W')
LinInt = Button(StatisticalCalculator, text='Linear Interpolation')
LinInt.grid(row=2,column=0, padx=11, pady=5, sticky='W')
Regression = Button(StatisticalCalculator, text='Regression')
Regression.grid(row=3,column=0, padx=11, pady=5, sticky='WN')
StatisticalCalculator.mainloop()
