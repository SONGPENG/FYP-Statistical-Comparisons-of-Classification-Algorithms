# -*- coding: utf-8 -*-
"""
@File  : LDA.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/10 21:04
@Desc  : 
"""

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
import pandas as pd


def lda_fun(file_path, result_path):
    """

    :param file_path:
    :param result_path:
    :return:
    """
    df = pd.read_csv(file_path, index_col=None, header=0)
    Y = df['target'].tolist()
    df = df.drop(['target'], axis=1)
    X = df.values

    data = LinearDiscriminantAnalysis(n_components=2).fit_transform(X, Y)

    plt.figure(figsize=(5, 4))
    plt.title('LDA')
    plt.scatter(data[:, 0], data[:, 1], s=3, c=Y)
    plt.colorbar()
    plt.savefig(result_path, dpi=300)
    plt.show()

# if __name__ == '__main__':
#     file_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/Adiac_TEST.csv'
#     result_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/PCA.png'
#     lda_fun(file_path, result_path)
