# -*- coding: utf-8 -*-
"""
@File  : TSNE.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/10 21:33
@Desc  : 
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf


# import tensorflow.compat.v1 as tf
#
# tf.disable_v2_behavior()


def cal_pairwise_dist(x):
    """
    Calculate the pairwise distance, and x is matrix.
    (a-b)^2 = a^2 + b^2 - 2*a*b

    @param x:
    @return:
    """

    sum_x = np.sum(np.square(x), 1)
    dist = np.add(np.add(-2 * np.dot(x, x.T), sum_x).T, sum_x)
    # returns the square of the distance between any two points.
    return dist


def cal_perplexity(dist, idx=0, beta=1.0):
    """
    Calculate perplexity, D is the distance vector.

    @param dist: the distance between itself and itself.
    @param idx:
    @param beta: Gaussian distribution parameter.
    @return:
    """

    prob = np.exp(-dist * beta)
    # Set prob to 0.
    prob[idx] = 0
    sum_prob = np.sum(prob)
    if sum_prob == 0:
        prob = np.maximum(prob, 1e-12)
        perp = -12
    else:
        perp = np.log(sum_prob) + beta * np.sum(dist * prob) / sum_prob
        prob /= sum_prob
    # The probability distribution of confusion and PI \j
    return perp, prob


def seach_prob(x, tol=1e-5, perplexity=30.0):
    """
    Binary search to find beta and calculate the prob of pairwise.

    @param x:
    @param tol:
    @param perplexity:
    @return:
    """

    # initialization parameter.
    # print("Computing pairwise distances...")
    (n, d) = x.shape
    dist = cal_pairwise_dist(x)
    pair_prob = np.zeros((n, n))
    beta = np.ones((n, 1))
    # take the log, and I'm going to do the math.
    base_perp = np.log(perplexity)

    for i in range(n):
        # if i % 500 == 0:
        # print("Computing pair_prob for point %s of %s ..." % (i, n))

        betamin = -np.inf
        betamax = np.inf
        # Dist [I] can't be all the points.
        perp, this_prob = cal_perplexity(dist[i], i, beta[i])

        # Binary search to find the best prob under sigma.
        perp_diff = perp - base_perp
        tries = 0
        while np.abs(perp_diff) > tol and tries < 50:
            if perp_diff > 0:
                betamin = beta[i].copy()
                if betamax == np.inf or betamax == -np.inf:
                    beta[i] = beta[i] * 2
                else:
                    beta[i] = (beta[i] + betamax) / 2
            else:
                betamax = beta[i].copy()
                if betamin == np.inf or betamin == -np.inf:
                    beta[i] = beta[i] / 2
                else:
                    beta[i] = (beta[i] + betamin) / 2

            # Update perb, prob value.
            perp, this_prob = cal_perplexity(dist[i], i, beta[i])
            perp_diff = perp - base_perp
            tries = tries + 1
        # Record the values of prob
        pair_prob[i,] = this_prob
    # print("Mean value of sigma: ", np.mean(np.sqrt(1 / beta)))
    # Conditional probability distribution PI \j of each point to the others.
    return pair_prob


def tsne(data, no_dims=2, perplexity=30.0, max_iter=800):
    """

    @param data: (n_samples, n_features)
    @param no_dims: target dimension
    @param perplexity:
    @param max_iter:
    @return: (n_samples, no_dims)
    """

    # init
    tf.reset_default_graph()

    (n, d) = data.shape
    # print(n, d)

    # symmetrization.
    P = seach_prob(data, 1e-5, perplexity)
    P = P + np.transpose(P)
    P = P / np.sum(P)  # pij
    P = np.maximum(P, 1e-12)
    # randomly initialize Y: y = np.random.randn(n, no_dims)
    # tf.random_normal_initializer(mean=0.0, stddev=1.0, seed=None, dtype=tf.float32)

    X = tf.placeholder(name="X", dtype=tf.float32, shape=[n, n])

    Y = tf.get_variable(name="Y", shape=[n, no_dims],
                        initializer=tf.random_normal_initializer())

    sum_y = tf.reduce_sum(tf.square(Y), 1)
    temp = tf.add(tf.transpose(tf.add(-2 * tf.matmul(Y, tf.transpose(Y)), sum_y)), sum_y)
    num = tf.divide(1, 1 + temp)
    one_ = tf.constant([x for x in range(n)])
    one_hot = tf.one_hot(one_, n)
    num = num - num * one_hot

    Q = num / tf.reduce_sum(num)
    Q = tf.maximum(Q, 1e-12)

    learning_rate = 500
    loss = tf.reduce_sum(X * tf.log(tf.divide(X, Q)))

    optimizer = tf.train.AdagradOptimizer(learning_rate=learning_rate)
    train_op = optimizer.minimize(loss)

    init = tf.global_variables_initializer()
    # print("begin")
    with tf.Session() as sess:
        init.run()
        for iter in range(max_iter):
            sess.run(train_op, feed_dict={X: P})
            if iter % 50 == 0:
                l = sess.run(loss, feed_dict={X: P})
                # print("%d\t%f" % (iter, l))
        y = sess.run(Y)
    # print("finished")

    return y


def tsne_fun(file_path, result_path):
    """

    :param file_path:
    :param result_path:
    :return:
    """

    df = pd.read_csv(file_path, index_col=None, header=0)
    Y = df['target'].tolist()
    df = df.drop(['target'], axis=1)
    X = df.values

    data_2d = tsne(X)

    plt.figure(figsize=(5, 4))
    plt.title('T-SNE')
    plt.scatter(x=data_2d[:, 0], y=data_2d[:, 1], s=3, c=Y)
    plt.colorbar()
    plt.savefig(result_path, dpi=300)
    plt.show()
#
# if __name__ == '__main__':
#     file_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/Adiac_TRAIN.csv'
#     result_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/PCA.png'
#     tsne_fun(file_path, result_path)
