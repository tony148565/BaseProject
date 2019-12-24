import numpy as np
import matplotlib.pyplot as plt
import json
while 1:
    ylist = []
    xlist = []
    num = input('輸入想製作的圖表1.長條圖2.折線圖3.結束:')
    if num == '1':
        plt.title('bar chart')
        plt.ylabel('score')
        plt.xlabel('subject')
        print('輸入為0中止輸入')
        while 1:
            tmp = input('subject:')
            if tmp == '0':
                break
            xlist.append(tmp)
        while len(ylist) < len(xlist):
            tmp = int(input('score:'))
            if tmp < 0:
                print('請輸入大於0的數字')
            if tmp > 100:
                print('請輸入小於100的數字')
            else:
                ylist.append(tmp)
        plt.ylim(bottom=0, top=100)
        plt.bar(xlist, ylist)
        plt.show()
    elif num == '2':
        plt.title('chart')
        plt.ylabel('score')
        plt.xlabel('subject')
        print('輸入為0中止輸入')
        while 1:
            tmp = input('subject:')
            if tmp == '0':
                break
            xlist.append(tmp)
        while len(ylist) < len(xlist):
            tmp = int(input('score:'))
            if tmp < 0:
                print('請輸入大於0的數字')
            if tmp > 100:
                print('請輸入小於100的數字')
            else:
                ylist.append(tmp)
        plt.ylim(0, 100)
        plt.plot(xlist, ylist, 'o-')
        plt.legend()
        plt.show()
    elif num == '3':
        break
    else:
        print('輸入錯誤')