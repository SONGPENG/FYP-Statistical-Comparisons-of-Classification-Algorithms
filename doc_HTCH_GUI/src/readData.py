# -*- coding: utf-8 -*-
"""
@File  : readData.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/11 15:16
@Desc  : 
"""
import pandas as pd


def read_data(source_path, is_error_rate=False):
    """

    :param source_path:
    :param is_error_rate:
    :return:
    """
    df = pd.read_csv(source_path, index_col=0, header=0)
    data = df.values if is_error_rate else (1 - df.values)

    classifier_name = df.axes[1].tolist()
    size = data.shape[0]
    return data, classifier_name, size
