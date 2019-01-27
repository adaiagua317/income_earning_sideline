#coding:utf-8
import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
def read_csv(filename):
    """
    read data from csv by tensorflow

    :param filename:filepath/filename
    :return: dataframe
    :exception: import error
    """

    if(os.path.exists(filename)):
        data=pd.read_csv(filename,header=0,encoding='utf-8')
    else:
        raise ImportError('file name not found!!!')

    return data


def series_stationrity_test(series):
    """
    time series stationrity test,three step:
    step 1:
    dot plot & basis statistics
    step 2:
    auto correlation & partial autocorrelation
    step 3:
    adf test

    :param series: time series
    :return:None

    """
    #step1:
    series=series.loc[series['dt']>='2018/7/1']
    series_sorted=series.sort_values(by='dt')
    fig=plt.figure()
    ax1=fig.add_subplot(221)
    ax1.plot(series_sorted['dt'],series_sorted['blue'],color='r')
    blue_cnt=series_sorted.pivot_table(index=['blue'],values=['red1'],aggfunc='count')
    ax2=fig.add_subplot(222)
    ax2.plot(blue_cnt.index,blue_cnt['red1'],color='y')


    #step2:
    ax3=fig.add_subplot(223)
    ax4=fig.add_subplot(224)
    plot_acf(series_sorted['blue'],lags=36,ax=ax3)
    plot_pacf(series_sorted['blue'],lags=36,ax=ax4)

    plt.show()

    #step3:
    dftest=adfuller(series_sorted['blue'])
    print(dftest)


unionLottoData=read_csv('../../data/lotto/unionLottoData.csv')
#print(unionLottoData['blue'])
series_stationrity_test(unionLottoData)

#————————————————————————————————————————————————结论—————————————————————————————————————————————————
#:v1:03-19年数据,频率表、acf、pacf、adf检验都是平稳的
#:v2:18-19年数据,频率表、acf、pacf、adf检验都是平稳的
#:v3:18.7-19年数据,频率表、acf、pacf、adf检验都是平稳的
#:v4:18.12-19年数据,频率表、acf、pacf、adf检验都是平稳的



