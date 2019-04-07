""" Some code are learned from learning sample at Kai Nai's blog from csdn tech blog.    
    https://blog.csdn.net/weixin_36279318/article/details/79082273
"""
import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

import seaborn as sns
import pandas as pd
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

class Analytics:
    def draw1(self):
        years = mdates.YearLocator()   # every year
        months = mdates.MonthLocator()  # every month
        yearFmt = mdates.DateFormatter('%m-%d')

        filename='sense_data1.csv'
        with open(filename,'r')as file:
            reader=csv.reader(file)
            header_row=next(reader)

            dates, temps, humids= [], [], []
            for row in reader:
                print(row)
                current_date = datetime.strptime(row[0],"%Y/%m/%d")
                dates.append(current_date)
                
                temps.append(float(row[1]))
                humids.append(float(row[2]))

            fig=plt.figure(dpi=128,figsize=(8, 5))
            
            plt.title('Temperature & Humidity in March/April 2019 - Average',fontsize=18)
            plt.plot(dates,temps,c='red')
            plt.xlabel('',fontsize=14)
            plt.ylabel('Temperature(*C)', fontsize=14, color='r')
            # plt.ylim(10,50)
            plt.tick_params(axis='both',which='major',labelsize=12)
            fig.autofmt_xdate()

            ax2 = plt.gca().twinx()
            ax2.plot(dates,humids,c='blue')
            plt.ylabel('Humidity(%)', fontsize=14, color='b')
            
            fig.savefig('plot1.png')
            plt.show()
            
    def draw2(self):
        filename='sense_data2.csv'
        filename='AllData.csv'
        my_data = pd.read_csv(filename)
        print(my_data)

        sns.set(style="whitegrid", color_codes=True)
        plt.figure(dpi=128, figsize=(8, 5))
        ax1 = sns.stripplot(x="Date", y="Temp", color = "red", jitter=True, data=my_data)
        ax1.set_title("Temperature & Humidity in Mar/April 2019 - All Data", fontsize=18)
        ax1.set_ylabel("Temperature (*C)", fontsize=18, color = "red")

        xlabels = [x for x in ax1.get_xticklabels()]
        ax1.set_xticklabels(xlabels)

        ax2 = plt.gca().twinx()
        ax2 = sns.stripplot(x="Date", y="Humid", color = "blue", jitter=True, data=my_data)
        ax2.set_ylabel("Humidity (%)", fontsize=18, color = "blue")

        plt.savefig('plot2.png')
        plt.show()
        
if __name__ == "__main__":
    ana = Analytics()
    ana.draw1()
    ana.draw2()