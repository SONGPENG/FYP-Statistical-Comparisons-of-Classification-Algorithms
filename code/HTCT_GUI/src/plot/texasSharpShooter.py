# -*- coding: utf-8 -*-
"""
@File  : texasSharpShooter.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/10 22:19
@Desc  : 
"""

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


def texas_sharp_shooter(name1, name2, is_error_rate, source_path, result_path):
    """

    @param name1: classifier A.
        example: name1 = 'DTW'
    @param name2: classifier B.
        example: name2 = 'LDWT'
    @param is_error_rate: boolean.
    @param source_path: '../../dataset/evaluation/accuracy/expectedActualAccuracy/DWT_LDWT_errorRate.csv'
    @param result_path:
    @return:
    """

    df = pd.read_csv(source_path, index_col=0, header=0)
    #                 Expected  Actual  Expected.1  Actual.1
    # Adiac           0.403   0.391       0.395     0.386
    # ArrowHead       0.083   0.200       0.083     0.171
    # Beef            0.500   0.333       0.500     0.333
    # BeetleFly       0.200   0.300       0.200     0.200

    plt.figure(figsize=(7, 6.5))
    texas_names = name1 + ' v.s. ' + name2
    plt.title(texas_names, fontsize=15)

    accur_rate = (1 - df.values) if is_error_rate else df.values
    expected_accuracy_gain = (accur_rate[:, 2] / accur_rate[:, 0])
    actual_accuracy_gain = (accur_rate[:, 3] / accur_rate[:, 1])

    x_min = np.min(expected_accuracy_gain)
    y_min = np.min(actual_accuracy_gain)
    min_value = math.floor(10 * min(x_min, y_min)) / 10
    x_max = np.max(expected_accuracy_gain)
    y_max = np.max(actual_accuracy_gain)
    max_value = math.ceil(10 * max(x_max, y_max)) / 10

    plt.xlim(min_value, max_value)
    plt.ylim(min_value, max_value)

    plt.axvline(x=1, lw=1, ls='-', c='black')
    plt.axhline(y=1, lw=1, ls='-', c='black')

    plt.fill([min_value, min_value, 1, 1], [min_value, 1, 1, min_value], color=[0.9843, 0.8471, 0.5765], alpha=0.3)
    plt.fill([1, max_value, max_value, 1], [1, 1, max_value, max_value], color=[0.9843, 0.8471, 0.5765], alpha=0.3)

    plt.scatter(x=expected_accuracy_gain, y=actual_accuracy_gain, s=20, c='r', alpha=1)

    plt.text(((x_min + 1) / 2), ((1 + y_max) / 2), 'FN', style='italic', fontsize=15)
    plt.text(((x_max + 1) / 2), ((1 + y_max) / 2), 'TP', style='italic', fontsize=15)
    plt.text(((x_min + 1) / 2), ((1 + y_min) / 2), 'TN', style='italic', fontsize=15)
    plt.text(((x_max + 1) / 2), ((1 + y_min) / 2), 'FP', style='italic', fontsize=15)

    plt.xlabel('Expected Accuracy Gain')
    plt.ylabel('Actual Accuracy Gain')

    plt.savefig(result_path, dpi=300)
    plt.show()

# using example:
# if __name__ == '__main__':
#     texas_sharp_shooter('DTW', 'LDWT', True,
#                         '../../dataset/evaluation/accuracy/expectedActualAccuracy/DWT_LDWT_errorRate.csv',
#                         '../../result/texasSharpShooter/DWT_LDWT.png')
#
#     texas_sharp_shooter('ED', 'LWED', True,
#                         '../../dataset/evaluation/accuracy/expectedActualAccuracy/ED_LWED_errorRate.csv',
#                         '../../result/texasSharpShooter/ED_LWED.jpg')
