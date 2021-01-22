# -*- coding: utf-8 -*-
"""
@File  : classifierComparePairwise.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/1 20:53
@Desc  :
"""

import matplotlib.pyplot as plt
import math
import pandas as pd
import numpy as np


def plot_compare_pairs(source_path, main_label, result_path, is_error_rate):
    """
    plot some accuracy scatter diagram for pairs of classifiers.

    @param source_path: e.g., '../../dataset/evaluation/accuracy/avgAccuracy/singleTrainTest.csv'
    @param main_label: main_label = 'NB
    @param result_path: '../../result/AAR/test_pair.jpg'
    @param is_error_rate:
    @return:
    """

    df = pd.read_csv(source_path, index_col=0, header=0)
    df = 1 - df if is_error_rate else df
    #                                     NB       C45      SVML      SVMQ
    # Adiac                         0.562660  0.542199  0.442455  0.762148
    # ArrowHead                     0.542857  0.605714  0.731429  0.742857
    # Beef                          0.666667  0.533333  0.900000  0.933333
    # BeetleFly                     0.750000  0.900000  0.800000  0.850000

    # other classifiers labels
    other_labels = df.axes[1].tolist()
    other_labels.remove(main_label)

    # main classifier data
    main_data = df[main_label].values

    # other classifier data
    df = df.drop(main_label, axis=1)
    other_data = df.values

    # the number of subplots
    figure_length = math.ceil(len(other_labels) ** 0.5)
    # plot the diagram
    size = len(other_labels)
    if size == 1:
        lw = 1
        s = 20
    else:
        lw = 0.8
        s = 2

    for y_data, y_label, i in zip(other_data.T, other_labels, range(size)):
        plt.subplot(figure_length, figure_length, i + 1, title=main_label + ' vs. ' + y_label)
        plt.xlim(0, 1.0)
        plt.ylim(0, 1.0)
        plt.xticks([0.2, 0.4, 0.6, 0.8])
        plt.yticks([0.2, 0.4, 0.6, 0.8])
        plt.xlabel(main_label)
        plt.ylabel(y_label)
        plt.fill([0, 0, 1], [0, 1, 1], color=[0.9843, 0.8471, 0.5765], alpha=0.3)
        if size == 1:
            plt.text(0.02, 0.9, 'In this area\n' + y_label + ' is better', style='italic', fontsize=10)
            plt.text(0.7, 0.02, 'In this area\n' + main_label + ' is better', style='italic', fontsize=10)
        plt.plot([0, 1.0], [0, 1.0], lw=lw, c='black')
        plt.scatter(x=main_data, y=y_data, s=s, c='r')

    plt.savefig(result_path, dpi=300)
    plt.show()

# using example:
# if __name__ == '__main__':
#     plot_compare_pairs('../../dataset/evaluation/accuracy/avgAccuracy/part1_singleTrainTest.csv', 'NB',
#                        '../../result/AAR/test_pair1.jpg', False)
#
#     plot_compare_pairs('../../dataset/evaluation/accuracy/avgAccuracy/part2_singleTrainTest.csv', 'NB',
#                        '../../result/AAR/test_pair2.jpg', True)
