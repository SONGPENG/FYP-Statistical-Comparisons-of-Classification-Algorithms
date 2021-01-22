# -*- coding: utf-8 -*-
"""
@File  : avgRunningTimings.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/10 21:56
@Desc  : 
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_average_timings(source_path, result_path):
    """

    @param source_path: source path, e.g. '../../dataset/evaluation/testTimingsLine.csv'
    @param eval_set: int value.
    @param result_path: result path, e.g. '../../result/ART/test.jpg'
    @return:
    """
    df = pd.read_csv(source_path, index_col=0, header=0)
    #                                     NB       C45      SVML      SVMQ
    # Adiac                         0.562660  0.542199  0.442455  0.762148
    # ArrowHead                     0.542857  0.605714  0.731429  0.742857
    # Beef                          0.666667  0.533333  0.900000  0.933333
    # BeetleFly                     0.750000  0.900000  0.800000  0.850000

    datasets_labels = df.axes[0].tolist()
    classifiers_labels = df.axes[1].tolist()
    data = df.values

    x = range(len(datasets_labels))
    for y_arr, label in zip(data.T, classifiers_labels):
        plt.plot(x, y_arr, 'o-', markersize=2, lw=1, label=label)

    plt.xlabel('Datasets Number = ' + str(len(datasets_labels)))
    plt.ylabel('Time  (ms)')
    plt.xticks(x, datasets_labels, rotation=90)
    plt.margins(0.08)
    plt.subplots_adjust(bottom=0.15)
    plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)

    plt.savefig(result_path, bbox_inches='tight', dpi=300)
    plt.show()


# using example:
# if __name__ == '__main__':
#     plot_average_timings('../../dataset/evaluation/testTimingsLine.csv', '../../result/ART/test.jpg')
