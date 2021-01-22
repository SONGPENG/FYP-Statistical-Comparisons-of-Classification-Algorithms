# -*- coding: utf-8 -*-
"""
@File  : roc.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/10 19:49
@Desc  : 
"""

import matplotlib.pyplot as plt
from sklearn import metrics
import pandas as pd
import numpy as np


def roc(source_path, result_path, pos_label):
    """
     plot a ROC diagram.

    @param source_path: '../../dataset/evaluation/roc/rocTest.csv'
    @param result_path: '../../result/ROC/test.jpg'
    @param pos_label: e.g. label = 1
    @return:
    """

    df = pd.read_csv(source_path, index_col=None, header=0)
    data = df.values

    scores = data.T[:-1]
    # e.g.
    # [[0.1, 0.2, 0.3, 0.1, 0.9, 1.0, 0.9, 0.8, 0.7],
    #  [0.8, 0.3, 0, 0.2, 0.6, 0.7, 0.6, 0.9, 0.8],
    #  [0.4, 0.1, 0.5, 0.16, 0.5, 0.65, 1.0, 0.75, 0.99],
    #  [0.9, 0.14, 0.25, 0.08, 0.7, 0.72, 0.8, 0.9, 0.77]]

    labels = data[:, -1]
    # e.g. [0, 0, 0, 0, 1, 1, 1, 1, 1]

    df = df.drop(['label'], axis=1)

    classifier_names = df.axes[1].tolist()
    # e.g. ['A', 'B', 'C', 'D']

    plt.figure()
    lw = 2
    for name, single_score in zip(classifier_names, scores):
        fpr, tpr, thresholds = metrics.roc_curve(labels, single_score, pos_label=pos_label)
        auc_value = metrics.auc(fpr, tpr)
        plt.plot(fpr, tpr, lw=lw, label=name + ': ROC curve (area = %0.2f)' % auc_value)

    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")

    plt.savefig(result_path, dpi=300)
    plt.show()

# using example:
# if __name__ == '__main__':
#     roc('../../dataset/evaluation/roc/rocTest.csv', '../../result/ROC/test.jpg', 1)
