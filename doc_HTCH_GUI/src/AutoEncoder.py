# -*- coding: utf-8 -*-
"""
@File  : AutoEncoder.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/10 21:00
@Desc  : 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf


def reset_graph(seed=42):
    """
    reset default graph.
    @param seed: random seed
    @return:
    """

    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)


def auto_encoder(data, hidden_layers=None, noise=0, drop_rate=0, n_epochs=301, learning_rate=0.01,
                 optimizer_type='adam', verbose=1):
    """

    @param data: (n_samples, n_features)
    @param hidden_layers: list hidden layers units num
    @param noise: normal noise
    @param drop_rate: drop_rate:
    @param n_epochs: n_epochs:
    @param learning_rate:
    @param optimizer_type:
    @param verbose:
    @return:
    """

    reset_graph()
    n_inputs = data.shape[1]
    n_outputs = n_inputs

    x = tf.placeholder(tf.float32, shape=[None, n_inputs])

    # add noise
    x_noise = x + noise * tf.random_normal(tf.shape(x))

    # dropout
    training = tf.placeholder_with_default(False, shape=(), name="training")
    x_drop = tf.layers.dropout(x_noise, drop_rate, training=training)

    hiddens = [x_drop]
    for i in range(len(hidden_layers)):
        n_layer = hidden_layers[i]
        hidden = tf.layers.dense(hiddens[i], n_layer, )
        hiddens.append(hidden)

    outputs = tf.layers.dense(hiddens[-1], n_outputs)
    hiddens.append(outputs)

    reconstruction_loss = tf.reduce_mean(tf.square(outputs - x))

    if optimizer_type == 'adam':
        optimizer = tf.train.AdamOptimizer(learning_rate)
    else:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate)

    training_op = optimizer.minimize(reconstruction_loss)

    init = tf.global_variables_initializer()

    # coding layer
    codings = hiddens[len(hiddens) // 2]

    with tf.Session() as sess:
        init.run()
        for epoch in range(n_epochs):
            sess.run(training_op, feed_dict={x: data, training: True})
            loss_train = reconstruction_loss.eval(feed_dict={x: data})
            # if epoch % 100 == 0 and verbose:
            #     print("\r{}".format(epoch), "Train MSE:", loss_train)
        data_ndim = codings.eval(feed_dict={x: data})

    return data_ndim


def auto_encoder_fun(file_path, result_path):
    """

    :param file_path:
    :param result_path:
    :return:
    """
    df = pd.read_csv(file_path, index_col=None, header=0)
    Y = df['target'].tolist()
    df = df.drop(['target'], axis=1)
    X = df.values

    data = auto_encoder(X, [2], learning_rate=0.2, n_epochs=1000)

    plt.figure(figsize=(5, 4))
    plt.title('AutoEncoder')
    plt.scatter(data[:, 0], data[:, 1], s=3, c=Y)
    plt.colorbar()
    plt.savefig(result_path, dpi=300)
    plt.show()

# if __name__ == '__main__':
#     file_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/Adiac_TRAIN2.csv'
#     result_path = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/Adiac/PCA.png'
#     auto_encoder_fun(file_path, result_path)
