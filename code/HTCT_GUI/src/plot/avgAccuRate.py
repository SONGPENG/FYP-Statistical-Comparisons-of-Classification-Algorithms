# -*- coding: utf-8 -*-
"""
@File  : avgAccuRate.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/3 13:38
@Desc  :
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_average_accuracy_rate(source_path, result_path, is_error_rate):
    """
    plot the overall accuracy for each classifiers.

    @param source_path: source path, e.g. '../../dataset/evaluation/accuracy/singleTrainTest.csv'
    @param result_path: the result path. e.g. '../../result/ROC/test_.jpg'
    @param is_error_rate:
    @return:
    """

    df = pd.read_csv(source_path, index_col=0, header=0)
    df = 1-df if is_error_rate else df
    #                                     NB       C45      SVML      SVMQ
    # Adiac                         0.562660  0.542199  0.442455  0.762148
    # ArrowHead                     0.542857  0.605714  0.731429  0.742857
    # Beef                          0.666667  0.533333  0.900000  0.933333
    # BeetleFly                     0.750000  0.900000  0.800000  0.850000

    # df = df.iloc[:10, :5]
    datasets_labels = df.axes[0].tolist()
    classifiers_labels = df.axes[1].tolist()
    data = df.values
    x = range(len(datasets_labels))
    for y_arr, label in zip(data.T, classifiers_labels):
        plt.plot(x, y_arr, 'x', markersize=5, lw=0.8, label=label)
    plt.xlabel('Datasets Number D= ' + str(len(datasets_labels)))
    plt.ylabel('Accuracy')
    plt.xticks(x, datasets_labels, rotation=90)
    plt.margins(0.08)
    plt.subplots_adjust(bottom=0.15)
    plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
    plt.savefig(result_path, bbox_inches='tight', dpi=300)
    plt.show()

# using example:
# if __name__ == '__main__':
#     plot_average_accuracy_rate('C:/Users/songp/Desktop/dataset/evaluation/accuracy/avgAccuracy/part3_singleTrainTest.csv',
#                                '../../result/AAR/2.jpg', True)
