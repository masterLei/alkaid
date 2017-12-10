#encoding:utf-8
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import tushare as ts
import datetime
import numpy as np
import pandas as pd
from matplotlib.dates import date2num

df = ts.get_hist_data('601318', ktype='D', start='2017-01-01')


df = df.sort_index(axis=0,ascending=True)



i = 0
result = pd.DataFrame(columns=('date','price','label'))
for index,row in df.iterrows():
    if(i == 4):
        array = df.iloc[0:i, 1]#low
        ind = array.argmin()
        result.loc[0] = {'date':ind,'price':array[ind],'label':'low'}

    if(i!= 0 and i%5 == 0 and i!=4):
        array = df.iloc[i-5:i,1]
        if result.iloc[len(result) - 1].label == 'low':
            ind = array.argmax()
            result.loc[len(result)] = {'date': ind, 'price': array[ind], 'label': 'high'}
        else:
            ind = array.argmin()
            result.loc[len(result)] = {'date': ind, 'price': array[ind], 'label': 'low'}
    i +=1

times = []
lows = []
for index,row in result.iterrows():
    date_time = datetime.datetime.strptime(row.date, '%Y-%m-%d')
    t = date2num(date_time)
    times.append(t)
    lows.append(row.price)

print("result",result)


x = np.array(times)
y = np.array(lows)

plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
plt.plot(x,y)
plt.show()
