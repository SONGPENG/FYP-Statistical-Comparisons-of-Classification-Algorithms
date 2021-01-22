# coding:utf-8
"""
author: Peng
email: peng.song@bjtu.edu.cn
date: 2020.03.08
"""

import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw


def fast_dtw(test_data, train_data):
    """

    :param test_data:
    :param train_data:
    :return:
    """
    row_size = train_data.shape[0]
    distances = np.zeros(row_size)
    for instance, i in zip(train_data, range(row_size)):
        d, path = fastdtw(test_data, instance, dist=euclidean)
        distances[i] = d

    sort_distance = distances.argsort()
    return sort_distance
