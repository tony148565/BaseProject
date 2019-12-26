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
flag = 1
printf = tk.StringVar()
a = False
hit = 0
check = 0
user_name = '訪客'
password = ''
check_point = 1

def main_choose(hit):
    global check_point
    global lea
    global check
    global L1
    global L2
    global L3
    global L4
    global L5
    global L6
    global E1
    global E2
    global E3
    global E4
    global E5
    global E6
    global t1
    global t2
    global t3
    global t4
    #print(check)

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
        elif check == 3:
            L1.grid_remove()
            L2.grid_remove()
            L3.grid_remove()
            L4.grid_remove()
            L5.grid_remove()
            L6.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            E3.grid_remove()
            E4.grid_remove()
            E5.grid_remove()
            E6.grid_remove()
            t1.grid_remove()
        elif check == 4:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
        elif check == 5:
            t1.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
        elif check == 6:
            L1.grid_remove()
        check = 1
        c = 20
        d = 20
        printf.set('-----------------\n\n\n學習追蹤')
        lea = tk.Label(ana_frame, textvariable=printf, font=('Arial', 16), width=c, height=d)
        lea.grid(row=0, column=0)
    if hit == 2:
        if check == 1:
            lea.grid_remove()
        elif check == 3:
            L1.grid_remove()
            L2.grid_remove()
            L3.grid_remove()
            L4.grid_remove()
            L5.grid_remove()
            L6.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            E3.grid_remove()
            E4.grid_remove()
            E5.grid_remove()
            E6.grid_remove()
            t1.grid_remove()
        elif check == 2:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
            t3.grid_remove()
            t4.grid_remove()
        elif check == 4:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
        elif check == 5:
            t1.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
        elif check == 6:
            L1.grid_remove()
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
                #for item in xlist:
                    #L5.insert(END, item)
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
        #L5 = Listbox(ana_frame, height=11)  # height=11设置listbox组件的高度，默认是10行。
        #L5.grid(row=4, column=4, sticky=W, padx=0)



    if hit == 3:
        eve = ''
        yy = StringVar
        mm = StringVar
        dd = StringVar
        hh = StringVar
        mi = StringVar
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
        elif check == 3:
            L1.grid_remove()
            L2.grid_remove()
            L3.grid_remove()
            L4.grid_remove()
            L5.grid_remove()
            L6.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            E3.grid_remove()
            E4.grid_remove()
            E5.grid_remove()
            E6.grid_remove()
            t1.grid_remove()
        elif check == 4:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
        elif check == 5:
            t1.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
        elif check == 6:
            L1.grid_remove()
        check = 3
        L1 = Label(ana_frame, text="事件")
        L1.grid(row=1, column=3, sticky=W, padx=1)
        L2 = Label(ana_frame, text="年分")
        L2.grid(row=1, column=4, sticky=W, padx=1)
        L3 = Label(ana_frame, text="月份")
        L3.grid(row=1, column=5, sticky=W, padx=1)
        L4 = Label(ana_frame, text="日")
        L4.grid(row=1, column=6, sticky=W, padx=1)
        L5 = Label(ana_frame, text="時")
        L5.grid(row=1, column=7, sticky=W, padx=1)
        L6 = Label(ana_frame, text="分")
        L6.grid(row=1, column=8, sticky=W, padx=1)
        E1 = Entry(ana_frame, bd=1, textvariable=eve)
        E1.grid(row=2, column=3, sticky=W, padx=1)
        E2 = Entry(ana_frame, bd=1, textvariable=yy)
        E2.grid(row=2, column=4, sticky=W, padx=1)
        E3 = Entry(ana_frame, bd=1, textvariable=mm)
        E3.grid(row=2, column=5, sticky=W, padx=1)
        E4 = Entry(ana_frame, bd=1, textvariable=dd)
        E4.grid(row=2, column=6, sticky=W, padx=1)
        E5 = Entry(ana_frame, bd=1, textvariable=hh)
        E5.grid(row=2, column=7, sticky=W, padx=1)
        E6 = Entry(ana_frame, bd=1, textvariable=mi)
        E6.grid(row=2, column=8, sticky=W, padx=1)

        def alarm():
            global flag
            from Alarm_clock import input_data
            input_data(E1.get(), int(E2.get()), int(E3.get()), int(E4.get()), int(E5.get()), int(E6.get()))
            from Alarm_clock import always_open
            always_open(flag)
            flag = 0
        t1 = Button(ana_frame, text='加入', command=alarm)
        t1.grid(row=3, column=6, sticky=W, padx=1)

        #printf.set('-------------------\n\n\n智慧提醒')
        #lea = tk.Label(ana_frame, textvariable=printf, font=('Arial', 16), width=c, height=d)
        #lea.grid(row=0, column=0)
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
        elif check == 3:
            L1.grid_remove()
            L2.grid_remove()
            L3.grid_remove()
            L4.grid_remove()
            L5.grid_remove()
            L6.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            E3.grid_remove()
            E4.grid_remove()
            E5.grid_remove()
            E6.grid_remove()
            t1.grid_remove()
        elif check == 4:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
        elif check == 5:
            t1.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
        elif check == 6:
            L1.grid_remove()
        check = 1
        c = 20
        d = 20
        #print('製作團隊:名字真難想\n馮伯誠\n毛文佐\n賴韜允\n羅弘翔\n')
        printf.set('製作團隊:名字真難想\n馮伯誠\n毛文佐\n賴韜允\n羅弘翔\n')
        lea = tk.Label(ana_frame, textvariable=printf, font=('Arial', 16), width=c, height=d)
        lea.grid(row=0, column=0)
    if hit == 5:
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
        elif check == 3:
            L1.grid_remove()
            L2.grid_remove()
            L3.grid_remove()
            L4.grid_remove()
            L5.grid_remove()
            L6.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            E3.grid_remove()
            E4.grid_remove()
            E5.grid_remove()
            E6.grid_remove()
            t1.grid_remove()
        elif check == 4:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
        elif check == 5:
            t1.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
        elif check == 6:
            L1.grid_remove()
        #print('dd')
        if user_name == '訪客':
            tkinter.messagebox.showerror("錯誤", "發文請先登入")
        else:
            check = 5
            def post_article():
                from database import make_a_post
                testt = make_a_post(E1.get(), E2.get(1.0, "end"))
                if testt == True:
                    tkinter.messagebox.showinfo("提示", "發文成功")
                    t1.grid_remove()
                    E1.grid_remove()
                    E2.grid_remove()
                else:
                    tkinter.messagebox.showerror("錯誤", "發文失敗")

            aa = StringVar()
            t1 = Button(ana_frame, text='發文', command=post_article)
            t1.grid(row=10, column=4, sticky=W, padx=1)
            E1 = Entry(ana_frame, bd=1, width=30, textvariable=aa)
            E1.grid(row=2, column=2, sticky=W, padx=1)
            E2 = Text(ana_frame, height=40, width=30)
            E2.grid(row=4, column=2, sticky=W, padx=1)
            # print('d')
    if hit == 7:
        #print('check_point is', check_point)
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
        elif check == 3:
            L1.grid_remove()
            L2.grid_remove()
            L3.grid_remove()
            L4.grid_remove()
            L5.grid_remove()
            L6.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            E3.grid_remove()
            E4.grid_remove()
            E5.grid_remove()
            E6.grid_remove()
            t1.grid_remove()
        elif check == 4:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
        elif check == 5:
            t1.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
        elif check == 6:
            L1.grid_remove()
        check = 4
        if user_name == '訪客':
            un = StringVar()
            pw = StringVar()
            L1 = Label(ana_frame, text="帳號")
            L1.grid(row=1, column=2, sticky=W, padx=1)
            L2 = Label(ana_frame, text="密碼")
            L2.grid(row=2, column=2, sticky=W, padx=1)
            E1 = Entry(ana_frame, bd=1, textvariable=un)
            E1.grid(row=1, column=3, sticky=W, padx=1)
            E2 = Entry(ana_frame, bd=1, textvariable=pw)
            E2.grid(row=2, column=3, sticky=W, padx=1)

            def register():
                if len(E1.get()) >= 100 or len(E2.get()) >= 100:
                    tkinter.messagebox.showerror("錯誤", "帳號密碼長度最多16個字元")
                else:
                    from database import register
                    tt = register(E1.get(), E2.get())
                    if(tt == True):
                        tkinter.messagebox.showerror("錯誤", "此帳號已經有人註冊")
                    else:
                        tkinter.messagebox.showinfo("提示", "註冊成功")

            def login_forum():
                global user_name
                global L1
                global L2
                global E1
                global E2
                global t1
                global t2
                global lea
                from database import uspw
                gg = uspw(E1.get(), E2.get())
                #print(type(gg))
                if(gg == True):
                    tkinter.messagebox.showinfo("提示", "登入成功")
                    user_name = E1.get()
                    print(user_name)
                    L1.grid_remove()
                    L2.grid_remove()
                    E1.grid_remove()
                    E2.grid_remove()
                    t1.grid_remove()
                    t2.grid_remove()
                    tex = "你好!!!" + user_name + "\n歡迎使用討論區及其他功能"
                    L1 = Label(ana_frame, text=tex, font=('Arial', 30))
                    L1.grid(row=3, column=5, sticky=W, padx=1)
                else:
                    tkinter.messagebox.showerror("錯誤", "帳號或密碼錯誤")
            t1 = Button(ana_frame, text="登入", command=login_forum)
            t1.grid(row=1, column=4, sticky=W, padx=1)
            t2 = Button(ana_frame, text="註冊", command=register)
            t2.grid(row=2, column=4, sticky=W, padx=1)
        else:
            check = 1
            tkinter.messagebox.showinfo("提示", "登入成功")
            tex = "你好!!!" + user_name + "\n歡迎使用討論區及其他功能"
            lea = Label(ana_frame, text=tex, font=('Arial', 30))
            lea.grid(row=3, column=5, sticky=W, padx=1)
    if hit == 6:
        #print('check_point is', check_point)
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
        elif check == 3:
            L1.grid_remove()
            L2.grid_remove()
            L3.grid_remove()
            L4.grid_remove()
            L5.grid_remove()
            L6.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            E3.grid_remove()
            E4.grid_remove()
            E5.grid_remove()
            E6.grid_remove()
            t1.grid_remove()
        elif check == 4:
            L1.grid_remove()
            L2.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
            t1.grid_remove()
            t2.grid_remove()
        elif check == 5:
            t1.grid_remove()
            E1.grid_remove()
            E2.grid_remove()
        elif check == 6:
            L1.grid_remove()
        check =6
        global grr
        grr = []
        from database import get_text
        L1 = tk.Listbox(ana_frame)
        for i in get_text():
            L1.insert(0, i)
        L1.grid(row=2, column=4, sticky=W, padx=1)
        #def
       # t1 = Button(ana_frame, text="看文", command= )


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


def gotoforum():
    global hit
    hit = 5
    main_choose(hit)


def login():
    global hit
    hit = 7
    main_choose(hit)

def looker():
    global hit
    hit = 6
    main_choose(hit)
top_frame.pack()
ana_frame.pack()
bottom_frame = tk.Frame(windows)
bottom_frame.pack(side=tk.BOTTOM)
Button(top_frame, text='關於開發者', command=maker_hit).pack(side='left')
Button(top_frame, text='學習追蹤', command=learning_trancer).pack(side='left')
Button(top_frame, text='學習成果分析', command=Results_analysis).pack(side='left')
Button(top_frame, text='智慧提醒', command=Smart_reminder).pack(side='left')
#Button(top_frame, text='開放式課程')
Button(top_frame, text='登入', command=login).pack(side='left')
Button(top_frame, text='討論區發文', command=gotoforum).pack(side='left')
Button(top_frame, text='討論區看文', command=looker).pack(side='left')


filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="關於開發者",command=maker_hit)
filemenu.add_command(label="學習追蹤",command=learning_trancer)
filemenu.add_command(label="學習成果分析",command=Results_analysis)
filemenu.add_command(label="智慧提醒",command=Smart_reminder)
menubar.add_cascade(label="選單",menu=filemenu)
windows.config(menu=menubar)


windows.mainloop()
