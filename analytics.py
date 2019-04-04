""" Some code are learned from learning sample at Kai Nai's blog from csdn tech blog.    
    https://blog.csdn.net/weixin_36279318/article/details/79082273
"""
import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearFmt = mdates.DateFormatter('%m-%d')

filename='sense_data.csv'
with open(filename,'r')as file:
    reader=csv.reader(file)
    header_row=next(reader)

    dates, temps, humids= [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        #4.将字符串转换为整型数据
        temps.append(int(row[1]))
        humids.append(int(row[2]))

    print(dates)
    print(temps)
    print(humids)
    #5.根据数据绘制图形
    fig=plt.figure(dpi=128,figsize=(8, 5.4))

    #6.将列表temps传个plot()方法
    # ax1 = plt.plot()
    # format the ticks
    # plt.xaxis.set_major_locator(years)
    # plt.gca().xaxis.set_major_formatter(yearFmt)
    # plt.xaxis.set_minor_locator(months)

    # ax1.fmt_xdata = mdates.DateFormatter('%m-%d')
    #7.设置图形的格式
    plt.title('Temperature and Humidity in March/April 2019',fontsize=20)
    plt.plot(dates,temps,c='red')
    plt.xlabel('',fontsize=22)
    plt.ylabel('Temperature(*C)', fontsize=14, color='r')
    plt.tick_params(axis='both',which='major',labelsize=14)
    fig.autofmt_xdate()

    ax2 = plt.gca().twinx()
    ax2.plot(dates,humids,c='blue')
    plt.ylabel('Humidity(%)', fontsize=14, color='b')
    
    plt.show()
