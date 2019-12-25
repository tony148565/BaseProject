# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime
import threading 
data = {}
things = list()
def input_data():
    thing = input("請輸入事件")
    year = int(input("請輸入年份"))
    month = int(input("請輸入月份"))
    day = int(input("請輸入日"))
    hour = int(input("請輸入時"))
    minute = int(input("請輸入分"))
    try:
        timestop = datetime.datetime(year,month,day,hour,minute,0)
        data[thing] = timestop
        things.append(thing)
    except ValueError:
        print("輸入格式錯誤!!!")

def check_time():
    while True:
        for i in range(0,len(things)):
            if datetime.datetime.now() >= data[things[i]]:
                print(things[i] + "時間到")
                del data[things[i]]
                things.remove(things[i])

while True:
    print("<如需查看指令請輸入help>")
    command = input("請輸入指令")
    if(command == 'help'):
        print("add ----- 加入一個新的提醒")
        print("show ----- 顯示已加入的提醒")
        print("end ----- 結束此功能")
    if(command == 'end'):
        print("離開中.....")
        break
    if(command == 'add'):
        input_data()
        threadobj = threading.Thread(target=check_time)
        threadobj.start()
    if(command == 'show'):
        for i in range(0,len(things)):
            print(things[i],end = ' ')
            print(data[things[i]].year,end = '-')
            print(data[things[i]].month,end = '-')
            print(data[things[i]].day,end = ' ')
            print(data[things[i]].hour,end = ':')
            print(data[things[i]].minute)

            
            