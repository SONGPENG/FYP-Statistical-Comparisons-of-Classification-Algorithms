import numpy as np


def euclidean_distance(test_data, train_data):
    """

    :param test_data:
    :param train_data:
    :return:
    """
    # Calculate the number of rows in the training sample.
    row_size = train_data.shape[0]
    # Calculate the difference between the training sample and the test sample.
    diff = np.tile(test_data, (row_size, 1)) - train_data
    # Calculate the sum of the squares of the differences.
    sqr_diff = diff ** 2
    sqr_diff_sum = sqr_diff.sum(axis=1)
    distances = sqr_diff_sum ** 0.5

    sort_distance = distances.argsort()
    return sort_distance
