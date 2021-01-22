# coding:utf-8
"""
author: Peng
email: peng.song@bjtu.edu.cn
date: 2020.03.08
"""

import numpy as np
import operator
import pandas as pd
import classifier.distance.EuclideanDistance as EuclideanDistance
import classifier.distance.FastDTW as FastDTW
import classifier.distance.Pearson as Pearson
import classifier.distance.SAX as SAX


def knn(test_data, train_data, labels, k, distance_dict, distance_style):
    """

    :param test_data:
    :param train_data:
    :param labels:
    :param k:
    :param distance_dict:
    :param distance_style:
    :return:
    """
    sort_distance = distance_dict[distance_style](test_data, train_data)
    count = {}

    for i in range(k):
        vote = labels[sort_distance[i]]
        count[vote] = count.get(vote, 0) + 1

    # Sort the frequency of category occurrence from high to low
    sort_count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    # Returns the most frequently occurring label
    return sort_count[0][0]


def utilize_knn(train_path, test_path, distance, k):
    """

    :param train_path:
    :param test_path:
    :param distance:
    :param k:
    :return:
    """
    distance_dict = {'Euclidean Distance': EuclideanDistance.euclidean_distance,
                     'fast DTW': FastDTW.fast_dtw,
                     'Pearson': Pearson.pearson,
                     'SAX': SAX.sax}

    df_train = pd.read_csv(train_path)
    labels = df_train['target'].tolist()
    df_train = df_train.drop(['target'], axis=1)
    train_data = df_train.values

    df_test = pd.read_csv(test_path)
    test_data = df_test.values
    test_size = test_data.shape[0]

    correct = 0
    for i, instance in zip(range(test_size), test_data):
        pre = knn(instance[:-1], train_data, labels, k, distance_dict, distance)
        # print('pre: ' + str(pre) + ' actual: ' + str(instance[-1]))
        if pre == instance[-1]:
            correct += 1

    result = 'K value: ' + str(k) + '\nDistance Type: ' + distance + '\nCorrect Number: ' + str(
        correct) + '\nTest Dataset Size: ' + str(
        test_size) + '\nTest Dataset Accuracy: ' + str(int(correct / test_size * 100) / 100)
    return result

# if __name__ == '__main__':
#     DATASET_ROOT_PATH = 'C:/Users/songp/Desktop/dataset/original/Univariate_arff/'
#     train_path = DATASET_ROOT_PATH + 'Adiac/Adiac_TRAIN.csv'
#     test_path = DATASET_ROOT_PATH + 'Adiac/Adiac_TEST.csv'
#     distance = 'Pearson'
#     result = utilize_knn(train_path, test_path, distance, 1)
#     print(result)
