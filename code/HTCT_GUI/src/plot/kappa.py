# -*- coding: utf-8 -*-
"""
@File  : kappa.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/4/19 12:52
@Desc  : 
"""
import pandas as pd
import numpy as np


def kappa_fun(file_name):
    """

    :param file_name:
    :return:
    """
    df = pd.read_csv(file_name, index_col=0, header=0)
    data = df.values

    total = np.sum(data)
    diagonal_total = np.sum(data.diagonal())
    accuracy = diagonal_total / total

    column_total = np.sum(data, axis=0)
    row_total = np.sum(data, axis=1)

    pec = 0
    for c_sum, r_sum in zip(column_total, row_total):
        pec = c_sum / total * r_sum / total + pec

    kappa = (accuracy - pec) / (1 - pec)

    return accuracy, pec, kappa


