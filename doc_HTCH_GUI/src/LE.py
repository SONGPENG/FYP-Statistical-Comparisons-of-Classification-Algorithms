# -*- coding: utf-8 -*-
"""
@File  : LE.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/10 21:04
@Desc  : 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def rbf(dist, t=1.0):
    """
    rbf kernel function
    @param dist:
    @param t:
    @return:
    """
    return np.exp(-(dist / t))


def cal_pairwise_dist(x):
    """
    Calculate the pairwise distance, and x is matrix.
    (a-b)^2 = a^2 + b^2 - 2*a*b

    @param x:
    @return:
    """

    sum_x = np.sum(np.square(x), 1)
    dist = np.add(np.add(-2 * np.dot(x, x.T), sum_x).T, sum_x)
    # Returns the square of the distance between any two points.
    return dist


def cal_rbf_dist(data, n_neighbors=10, t=1):
    dist = cal_pairwise_dist(data)
    dist[dist < 0] = 0
    n = dist.shape[0]
    rbf_dist = rbf(dist, t)

    w = np.zeros((n, n))
    for i in range(n):
        index_ = np.argsort(dist[i])[1:1 + n_neighbors]
        w[i, index_] = rbf_dist[i, index_]
        w[index_, i] = rbf_dist[index_, i]

    return w


def le(data, n_dims=2, n_neighbors=5, t=1.0):
    """

    @param data: (n_samples, n_features)
    @param n_dims: target dim
    @param n_neighbors: k nearest neighbors
    @param t: a param for rbf
    @return:
    """

    n = data.shape[0]
    w = cal_rbf_dist(data, n_neighbors, t)
    d = np.zeros_like(w)
    for i in range(n):
        d[i, i] = np.sum(w[i])

    D_inv = np.linalg.inv(d)
    L = d - w
    eig_val, eig_vec = np.linalg.eig(np.dot(D_inv, L))
    sort_index_ = np.argsort(eig_val)
    eig_val = eig_val[sort_index_]

    j = 0
    while eig_val[j] < 1e-6:
        j += 1

    sort_index_ = sort_index_[j:j + n_dims]
    eig_vec_picked = eig_vec[:, sort_index_]
    x_ndim = eig_vec_picked
    return x_ndim


def le_fun(file_path, result_path):
    """

    :param file_path:
    :param result_path:
    :return:
    """
    df = pd.read_csv(file_path, index_col=None, header=0)
    Y = df['target'].tolist()
    df = df.drop(['target'], axis=1)
    X = df.values

    dist = cal_pairwise_dist(X)
    max_dist = np.max(dist)
    X_ndim = le(X, n_neighbors=20, t=max_dist * 0.1)

    fig = plt.figure(figsize=(5, 4))
    plt.title('LE')
    plt.scatter(x=X_ndim[:, 0], y=X_ndim[:, 1], s=3, c=Y)
    plt.colorbar()
    plt.savefig(result_path, dpi=300)
    plt.show()

# if __name__ == '__main__':
#     file_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/Adiac_TRAIN2.csv'
#     result_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/PCA.png'
#     le_fun(file_path, result_path)
