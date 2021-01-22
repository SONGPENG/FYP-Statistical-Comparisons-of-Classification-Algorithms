# coding:utf-8
"""
author: Peng
email: peng.song@bjtu.edu.cn
date: 2020.03.08
"""

from scipy.stats import pearsonr
import numpy as np


def pearson(test_data, train_data):
    """

    :param test_data:
    :param train_data:
    :return:
    """
    row_size = train_data.shape[0]
    distances = np.zeros(row_size)

    for instance, i in zip(train_data, range(row_size)):
        pccs, _ = pearsonr(test_data, instance)
        distances[i] = pccs

    sort_distance = np.argsort(-distances)
    return sort_distance
