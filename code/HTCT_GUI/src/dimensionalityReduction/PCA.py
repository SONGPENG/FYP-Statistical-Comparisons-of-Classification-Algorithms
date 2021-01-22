# -*- coding: utf-8 -*-
"""
@File  : PCA.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/10 21:26
@Desc  : 
"""

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图
import pandas as pd


def pca_fun(file_path, result_path):
    """

    :param file_path:
    :param result_path:
    :return:
    """
    df = pd.read_csv(file_path, index_col=None, header=0)
    Y = df['target'].tolist()
    df = df.drop(['target'], axis=1)
    X = df.values

    sklearn_pca = PCA(n_components=2)
    data_2d2 = sklearn_pca.fit_transform(X)

    plt.figure(figsize=(5, 4))
    plt.title('PCA')
    plt.scatter(x=data_2d2[:, 0], y=data_2d2[:, 1], s=3, c=Y)
    plt.colorbar()
    plt.savefig(result_path, dpi=300)
    plt.show()


# if __name__ == "__main__":
#     file_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/Adiac_TRAIN.csv'
#     result_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/PCA.png'
#     pca_fun(file_path, result_path)
