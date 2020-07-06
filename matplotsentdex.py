import matplotlib.pyplot as plt
import csv
import numpy as np
import urllib.request
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import mplfinance
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib import style


#style.use('ggplot')
style.use('fivethirtyeight')




# x= [1, 2, 3]
# y = [5, 7, 4]
# x2 = [1,2,3]
# y2 = [10, 14, 12]
#
#
# plt.plot(x, y, label= 'First line')
# plt.plot(x2, y2, label= 'Second Line')
#
# plt.xlabel('ex')
# plt.ylabel('whys')
# plt.title('Cool graph\nCheck it out')
# plt.legend()
# plt.show() #line with labels


# x= [2,4,6,8,10]
# y = [6,7,8,2,4]
# x2 = [1, 3, 5, 7, 9]
# y2 = [7, 8, 2, 4, 2]
#
# plt.bar(x,y, label= 'Bars1', color = 'blue')
# plt.bar(x2, y2, label = 'Bars2', color  = 'red')
#
# plt.xlabel('ex')
# plt.ylabel('whys')
# plt.title('Cool graph\nCheck it out')
# plt.legend()
# plt.show() #barchart

# population_ages= [22,55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]
# #ids = [x for x in range(len(population_ages))]
# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
#
# plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)



#plt.bar(ids, population_ages, label= 'Bars1', color = 'blue')
#plt.bar(x2, y2, label = 'Bars2', color  = 'red')

# x= [1, 2, 3, 4, 5, 6, 7, 8]
# y =[5, 2, 4, 2, 1, 4, 5, 2]
#
#
#
# plt.scatter(x, y, label = 'skitscat', color = 'k',marker= 'o', s=100)
#
# plt.xlabel('ex')
# plt.ylabel('whys')
# plt.title('Cool graph\nCheck it out')
# plt.legend()
# plt.show() #histogram

# days= [1, 2, 3, 4, 5]
# sleeping = [7,8,6,11,7]
# eating= [2, 3, 4, 3, 2]
# working= [7, 8,7,2,2]
# playing = [8,5,7,8,13]
#
# plt.plot([], [], color = 'm', label = 'sleeping')
# plt.plot([], [], color = 'c', label = 'eating')
# plt.plot([], [], color = 'r', label = 'working')
# plt.plot([], [], color = 'k', label = 'playing')
#
# plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])
#
#
#
# #plt.scatter(x, y, label = 'skitscat', color = 'k',marker= 'o', s=100)
#
# plt.xlabel('ex')
# plt.ylabel('whys')
# plt.title('Cool graph\nCheck it out')
# plt.legend()
# plt.show() #stackplot

# days= [1, 2, 3, 4, 5]
# sleeping = [7,8,6,11,7]
# eating= [2, 3, 4, 3, 2]
# working= [7, 8,7,2,2]
# playing = [8,5,7,8,13]
#
# slices = [7, 2, 2, 13]
# activities = ['sleeping', 'eating', 'working', 'playing']
# cols = ['m','c','r','k']
#
# plt.pie(slices, labels= activities,
#         colors= cols, startangle = 90,
#         shadow= True, explode= (0, 0.1, 0, 0),
#         autopct= '%1.1f%%')



# plt.xlabel('ex')
# plt.ylabel('whys')
# plt.title('Cool graph\nCheck it out')
# #plt.legend()
# plt.show() #histogram



# x = []
# y = []
# with open('datatomatplotlib.txt', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter = ',')
#     for row in plots:
#         x.append(float(row[0]))
#         y.append(float(row[1]))
#
#
# # x, y =np.loadtxt('datatomatplotlib.txt', delimiter= ',', unpack=True)
# plt.plot(x, y, label = 'Loaded from file')
#
# plt.xlabel('ex')
# plt.ylabel('whys')
# plt.title('Cool graph\nCheck it out')
# plt.legend()
# plt.show() #data from txtfile
# def bytespdate2num(fmt, encoding='utf-8' ):
#     strconverter= mdates.strpdate2num(fmt)
#     def bytesconverter(b):
#         s = b.decode(encoding)
#         return strconverter(s)
#     return bytesconverter
#
# def graph_data(stock):
#
#     fig = plt.figure()
#     ax1= plt.subplot2grid((1, 1), (0,0))
#
#     stock_price_url =  'https://pythonprogramming.net/yahoo_finance_replacement'
#     source_code = urllib.request.urlopen(stock_price_url).read().decode()
#     stock_data = []
#     split_source = source_code.split('\n')
#     for line in split_source:
#         split_line = line.split(',')
#         if len(split_line) == 7:
#             if 'Volume' not in line and 'labels' not in line:
#                 stock_data.append(line)
#
#     date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
#                                                                      delimiter=',',
#                                                                      unpack=True,
#                                                                      converters={0: bytespdate2num('%Y-%m-%d')})
#
#
#     ax1.plot_date(date, closep, '-', label = 'Price')
#     for label in ax1.xaxis.get_ticklabels():
#         label.set_rotation(45)
#     ax1.grid(True)
#
#     plt.xlabel('Date')
#     plt.ylabel('Price')
#     plt.title('Cool graph\nCheck it out')
#     plt.legend()
#     plt.subplots_adjust(left = 0.09, bottom = 0.18, right = 0.94, top = 0.95, wspace=0.2, hspace=0)
#     plt.show()
#
# graph_data('TSLA')

# def bytespdate2num(fmt, encoding='utf-8' ):
#     strconverter= mdates.strpdate2num(fmt)
#     def bytesconverter(b):
#         s = b.decode(encoding)
#         return strconverter(s)
#     return bytesconverter
#
# def graph_data(stock):
#
#     fig = plt.figure()
#     ax1= plt.subplot2grid((1, 1), (0,0))
#
#     stock_price_url =  'https://pythonprogramming.net/yahoo_finance_replacement'
#     source_code = urllib.request.urlopen(stock_price_url).read().decode()
#     stock_data = []
#     split_source = source_code.split('\n')
#     for line in split_source:
#         split_line = line.split(',')
#         if len(split_line) == 7:
#             if 'Volume' not in line and 'labels' not in line:
#                 stock_data.append(line)
#
#     date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
#                                                                      delimiter=',',
#                                                                      unpack=True,
#                                                                      converters={0: bytespdate2num('%Y-%m-%d')})
#
#
#     ax1.plot_date(date, closep, '-', label = 'Price')
#
#     ax1.fill_between(date, closep, where=(closep > closep[0] ), facecolor='g', alpha=0.3)
#     ax1.fill_between(date, closep, where=(closep < closep[0]), facecolor='r', alpha=0.3)
#     for label in ax1.xaxis.get_ticklabels():
#         label.set_rotation(45)
#     ax1.grid(True)
#     ax1.xaxis.label.set_color('c')
#     ax1.yaxis.label.set_color('c')
#
#     plt.xlabel('Date')
#     plt.ylabel('Price')
#     plt.title('Cool graph\nCheck it out')
#     plt.legend()
#     plt.subplots_adjust(left = 0.09, bottom = 0.18, right = 0.94, top = 0.95, wspace=0.2, hspace=0)
#     plt.show()
#
# graph_data('TSLA')

# def bytespdate2num(fmt, encoding='utf-8' ):
#     strconverter= mdates.strpdate2num(fmt)
#     def bytesconverter(b):
#         s = b.decode(encoding)
#         return strconverter(s)
#     return bytesconverter

# def graph_data(stock):
#
#     fig = plt.figure()
#     ax1= plt.subplot2grid((1, 1), (0,0))
#
#     stock_price_url =  'https://pythonprogramming.net/yahoo_finance_replacement'
#     source_code = urllib.request.urlopen(stock_price_url).read().decode()
#     stock_data = []
#     split_source = source_code.split('\n')
#     for line in split_source:
#         split_line = line.split(',')
#         if len(split_line) == 7:
#             if 'Volume' not in line and 'labels' not in line:
#                 stock_data.append(line)
#
#     date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
#                                                                      delimiter=',',
#                                                                      unpack=True,
#                                                                      converters={0: bytespdate2num('%Y-%m-%d')})
#
#
#     ax1.plot_date(date, closep, '-', label = 'Price')
#     ax1.axhline(closep[0], color = 'k', linewidth = 5)
#
#     ax1.fill_between(date, closep, where=(closep > closep[0] ), facecolor='g', alpha=0.3)
#     ax1.fill_between(date, closep, where=(closep < closep[0]), facecolor='r', alpha=0.3)
#     for label in ax1.xaxis.get_ticklabels():
#         label.set_rotation(45)
#     ax1.grid(True)
#
#     # ax1.xaxis.label.set_color('c')
#     # ax1.yaxis.label.set_color('c')
#     ax1.spines['left'].set_color('c')
#     ax1.spines['right'].set_visible(False)
#     ax1.spines['top'].set_visible(False)
#     ax1.tick_params(axis='x', colors = '#95b600')
#
#     plt.xlabel('Date')
#     plt.ylabel('Price')
#     plt.title('Cool graph\nCheck it out')
#     plt.legend()
#     plt.subplots_adjust(left = 0.09, bottom = 0.18, right = 0.94, top = 0.95, wspace=0.2, hspace=0)
#     plt.show()
#
# graph_data('TSLA')

def bytespdate2num(fmt, encoding='utf-8' ):
    strconverter= mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data(stock):

    fig = plt.figure()
    ax1= plt.subplot2grid((1, 1), (0,0))

    stock_price_url =  'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Volume' not in line and 'labels' not in line:
                stock_data.append(line)

    date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0: bytespdate2num('%Y-%m-%d')})

    x = 0
    y = len(date)
    ohlc = []
    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x+=1

    mplfinance.original_flavor.candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown= 'r')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(6))


    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('TSLA')
    plt.legend()
    plt.subplots_adjust(left = 0.09, bottom = 0.18, right = 0.94, top = 0.95, wspace=0.2, hspace=0)
    plt.show()

graph_data('TSLA')