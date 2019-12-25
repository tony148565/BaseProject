from bs4 import BeautifulSoup
import request
import numpy as np

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
import tkinter as tk
#import matplotlib
#print(matplotlib.matplotlib_fname())
import tkinter.messagebox

windows = Tk()
menubar = Menu(windows)
top_frame = tk.Frame(windows)
ana_frame = tk.Frame(windows)
windows.title('行動逢甲3.0')
windows.geometry('1024x800')
l = tk.Label(windows, text='行動逢甲3.0', bg='red', font=('Arial', 16), width=1024, height=2)
l.pack()
printf = tk.StringVar()
a = False
hit = 0
check = 0
def main_choose(hit):
    global lea
    global check
    global L1
    global L2
    global E1
    global E2
    global t1
    global t2
    global t3
    global t4
    print(check)

    if hit == 1:
        if check == 1:
            lea.grid_remove()
        elif check == 2:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
            t3.grid_remove()
            t4.grid_remove()
        check = 1
        c = 20
        d = 20
        printf.set('-----------------\n\n\n學習追蹤')
        lea = tk.Label(ana_frame, textvariable=printf, font=('Arial', 16), width=c, height=d)
        lea.grid(row=0, column=0)
    if hit == 2:
        if check == 1:
            lea.grid_remove()
        check = 2
        #printf.set('學習成果分析')
        ylist = []
        xlist = []
        a1 = StringVar()
        a2 = StringVar()
        L1 = Label(ana_frame, text="科目")
        L1.grid(row=1, column=3)
        L2 = Label(ana_frame, text="成績")
        L2.grid(row=1, column=4)
        E1 = Entry(ana_frame, bd=1, textvariable=a1)
        E1.grid(row=2, column=3)
        E2 = Entry(ana_frame, bd=1, textvariable=a2)
        E2.grid(row=2, column=4)
        def show_entry_fields():
            #print("First Name: %s\nLast Name: %s" % (list, E2.get()))
            if E1.get() == '' or E2.get() == '':
                tkinter.messagebox.showerror("錯誤", "輸入不得為空")
            else:
                xlist.append(E1.get())
                a=int(E2.get())
                ylist.append(a)
                E1.delete(0, END)
                E2.delete(0, END)
            print(xlist)
            print(ylist)
        def del_entry():
            if len(xlist) == 0 or len(ylist) == 0:
                tkinter.messagebox.showerror("錯誤", "未輸入資料")
            else:
                c = E1.get()
                #print(type(c))
                x = xlist.remove(c)
                b = ylist.remove(int(E2.get()))
                if a == '':
                    tkinter.messagebox.showwarning("警告", "無此科目")
                E1.delete(0, END)
                E2.delete(0, END)
                print(x)
                print(b)
        num='1'
        def bargraph():
            global num
            if len(xlist) == 0:
                tkinter.messagebox.showerror("錯誤", "輸入不得為空")
            else:
                num = '1'
                analysis_system()
        def linechart():
            global num
            if len(xlist) == 0:
                tkinter.messagebox.showerror("錯誤", "輸入不得為空")
            else:
                num = '2'
                analysis_system()
        def analysis_system():
            global num
            if num == '1':
                print('正在製作長條圖--------')
                plt.plot(label='成果分析')
                plt.title("成果分析")
                plt.ylabel('score')
                plt.xlabel('subject')
                plt.ylim(bottom=0, top=100)
                plt.bar(xlist, ylist)
                plt.show()
            elif num == '2':
                print('正在製作折線圖--------')
                plt.title('成果分析')
                plt.ylabel('score')
                plt.xlabel('subject')
                plt.ylim(0, 100)
                plt.plot(xlist, ylist, 'o-')
                plt.legend()
                plt.show()
        t1 = Button(ana_frame, text='  加入  ', command=show_entry_fields)
        t1.grid(row=3, column=3, sticky=W, padx=0)
        t2 = Button(ana_frame, text='  刪除  ', command=del_entry)
        t2.grid(row=3, column=4, sticky=W, padx=0)
        t3 = Button(ana_frame, text='製作長條圖', command=bargraph)
        t3.grid(row=3, column=5, sticky=W, padx=0)
        t4 = Button(ana_frame, text='製作折線圖', command=linechart)
        t4.grid(row=3, column=6, sticky=W, padx=0)
        #print(a1.get())
        #print(a2.get())
        #print(type(t1))
        #print(type(t2))
        #print(type(t3))
    if hit == 3:
        if check == 1:
            lea.grid_remove()
        elif check == 2:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
            t3.grid_remove()
            t4.grid_remove()
        check = 1
        c = 20
        d = 20
        printf.set('-------------------\n\n\n智慧提醒')
        lea = tk.Label(ana_frame, textvariable=printf, font=('Arial', 16), width=c, height=d)
        lea.grid(row=0, column=0)
    if hit == 4:
        if check == 1:
            lea.grid_remove()
        elif check == 2:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
            t3.grid_remove()
            t4.grid_remove()
        check = 1
        c = 20
        d = 20
        #print('製作團隊:名字真難想\n馮伯誠\n毛文佐\n賴韜允\n羅弘翔\n')
        printf.set('製作團隊:名字真難想\n馮伯誠\n毛文佐\n賴韜允\n羅弘翔\n')
        lea = tk.Label(ana_frame, textvariable=printf, font=('Arial', 16), width=c, height=d)
        lea.grid(row=0, column=0)
def learning_trancer():
    global hit
    hit = 1
    main_choose(hit)
def maker_hit():
    global hit
    hit = 4
    main_choose(hit)
def Results_analysis():
    global hit
    hit = 2
    main_choose(hit)
def Smart_reminder():
    global hit
    hit = 3
    main_choose(hit)

top_frame.pack()
ana_frame.pack()
bottom_frame = tk.Frame(windows)
bottom_frame.pack(side=tk.BOTTOM)
Button(top_frame, text='關於開發者', command=maker_hit).pack()
Button(top_frame, text='學習追蹤', command=learning_trancer).pack()
Button(top_frame, text='學習成果分析', command=Results_analysis).pack()
Button(top_frame, text='智慧提醒', command=Smart_reminder).pack()

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="關於開發者",command=maker_hit)
filemenu.add_command(label="學習追蹤",command=learning_trancer)
filemenu.add_command(label="學習成果分析",command=Results_analysis)
filemenu.add_command(label="智慧提醒",command=Smart_reminder)
menubar.add_cascade(label="選單",menu=filemenu)
windows.config(menu=menubar)


windows.mainloop()
