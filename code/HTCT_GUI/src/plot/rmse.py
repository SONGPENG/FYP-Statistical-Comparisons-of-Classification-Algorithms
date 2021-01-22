# -*- coding: utf-8 -*-
"""
@File  : rmse.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/4/19 12:53
@Desc  : 
"""

import pandas as pd


def rmse_fun(file_name):
    """

    :param file_name:
    :return:
    """
    df = pd.read_csv(file_name, index_col=None, header=0)
    data = df.values
    number = data.shape[0]

    temp = 0
    for row in data:
        temp = temp + (row[1] - row[0]) ** 2

    rmse = (temp / number) ** 0.5
    return int(rmse * 1000) / 1000
