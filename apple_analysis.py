# -*- coding:utf-8 -*-

import pandas as pd

def quarter_volume():
    # 读取csv文件
    data = pd.read_csv('apple.csv',header=0)
    # 2.转换为时间序列
    data['Date'] = pd.to_datetime(data['Date'])
    # 1.使用Pandas选择数据
    res = data.Volume
    res.index = data.Date
    #3.按季度重采样
    results = res.resample('Q').sum()

    # 排序
    #sorted_res = sorted(results)
    sorted_res = results.sort_values()
    second_volume = sorted_res[-2]

    print(second_volume)
    return second_volume

quarter_volume()
