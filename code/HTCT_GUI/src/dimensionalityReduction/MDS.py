# -*- coding: utf-8 -*-
"""
@File  : MDS.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/10 21:24
@Desc  : 
"""

from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import pandas as pd


def mds_fun(file_path, result_path):
    """

    :param file_path:
    :param result_path:
    :return:
    """
    df = pd.read_csv(file_path, index_col=None, header=0)
    Y = df['target'].tolist()
    df = df.drop(['target'], axis=1)
    X = df.values

    data_2 = MDS(n_components=2).fit_transform(X)

    plt.figure(figsize=(5, 4))
    plt.title('MDS')
    plt.scatter(data_2[:, 0], data_2[:, 1], s=3, c=Y)
    plt.colorbar()
    plt.savefig(result_path, dpi=300)
    plt.show()


# if __name__ == '__main__':
#     file_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/Adiac_TRAIN2.csv'
#     result_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/PCA.png'
#     mds_fun(file_path, result_path)
