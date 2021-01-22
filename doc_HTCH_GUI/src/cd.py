# -*- coding: utf-8 -*-
"""
@File  : cd_ui.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/2 12:38
@Desc  :
"""

import matlab
import matlab.engine
import pandas as pd


def plot_cd(source_path, cd_path, is_error_rate):
    """
    Plot the CD diagram, and return the CD value.
    Invoke one Matlab function - critical_difference to realize the function.

    @param source_path: '../../dataset/evaluation/accuracy/avgAccuracy/singleTrainTest.csv'
    @param cd_path: '../../result/CD/test.jpg'
    @param is_error_rate: boolean
    @return:
    """

    df = pd.read_csv(source_path, index_col=0, header=0)
    #                                     NB       C45      SVML      SVMQ
    # Adiac                         0.562660  0.542199  0.442455  0.762148
    # ArrowHead                     0.542857  0.605714  0.731429  0.742857
    # Beef                          0.666667  0.533333  0.900000  0.933333
    # BeetleFly                     0.750000  0.900000  0.800000  0.850000

    # the engine to invoke Matlab function.
    eng = matlab.engine.start_matlab('../')

    # read the data from the specified file.
    # the data's header, generally the algorithm labels.
    labels = df.axes[1].tolist()
    # the error rate of each algorithms for each classifiers.
    error_rate = df.values if is_error_rate else (1 - df.values)

    # invoke Matlab function to plot CD diagram.
    cd = eng.critical_difference(cd_path, matlab.double(error_rate.tolist()), labels)
    eng.exit()


# using example:
# if __name__ == '__main__':
#     plot_cd('C:/Users/songp/Desktop/HTC/_DATASET/HTC test/1 hypothesis testing/multiple classifiers.csv',
#             'C:/Users/songp/Desktop/cd.png',
#             is_error_rate=False)
