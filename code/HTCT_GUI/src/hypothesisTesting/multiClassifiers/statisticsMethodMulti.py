# -*- coding: utf-8 -*-
"""
@File  : statisticsMethod2.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/11 15:19
@Desc  : 
"""

import scipy.stats as stats
import hypothesisTesting.readData as rd


def result_template(classifier_name, size, confidence, name, s, p, conclusion1='\nNull Hypothesis rejected',
                    conclusion2='\nNull Hypothesis accepted'):
    """

    :param classifier_name:
    :param size:
    :param confidence:
    :param name:
    :param s:
    :param p:
    :param conclusion1:
    :param conclusion2:
    :return:
    """
    result = 'Program to analyze Performance among [' + ', '.join(
        str(i) for i in classifier_name) + '] using ' + name + '.'
    result += '\n\nNumber of test point: ' + str(size)
    result += '\nConfidence level: ' + str(confidence)
    result += '\nStatistics: ' + str(round(s, 2)) + ',  P value: ' + str(round(p, 4))
    if p < confidence:
        result += '\n\nP value < Confidence, ' + conclusion1
    else:
        result += '\n\nP value > Confidence, ' + conclusion2
    result += '.\n'
    return result


def one_way_variance(source_path, is_error_rate, confidence=0.05):
    """
    Parameter method.
    One-way Analysis of Variance to compare multiple classifiers on multiple datasets.

    @param source_path:
    @param is_error_rate:
    @param confidence:
    @return:
    """
    data, classifier_name, size = rd.read_data(source_path, is_error_rate)
    w, p = stats.levene(*data.T)
    result = 'Begin ------------------------------\n' + \
             result_template(classifier_name, size, confidence, 'Levene Test', w, p,
                             conclusion1='\nHomogeneity of Variances Hypothesis rejected',
                             conclusion2='\nHomogeneity of Variances Hypothesis accepted')

    f, p = stats.f_oneway(*data.T)
    result += '\n\n\n' + result_template(classifier_name, size, confidence, 'One-way Variance Analysis', f,
                                         p) + 'End --------------------------------\n'

    return result


def kruskal(source_path, is_error_rate, confidence=0.05, nan_policy='omit'):
    """
    Nonparametric method.
    H test.

    @param source_path:
    @param is_error_rate:
    @param confidence:
    @param nan_policy: {'propagate', 'raise', 'omit'}, optional.
    Defines how to handle when input contains nan. The following options are available.
    default is 'propagate':
        *   'propagate': returns nan
        *   'raise': throws an error
        *   'omit': performs the calculations ignoring nan values
    @return:
    """
    data, classifier_name, size = rd.read_data(source_path, is_error_rate)

    k, p = stats.kruskal(*data.T, nan_policy=nan_policy)
    result = 'Begin ------------------------------\n' + result_template(classifier_name, size, confidence,
                                                                        'Kruskal Test', k,
                                                                        p) + 'End --------------------------------\n'

    return result


def friedman(source_path, is_error_rate, confidence=0.05):
    """
    Nonparametric method.

    @param source_path:
    @param is_error_rate:
    @param confidence:
    @return:
    """
    data, classifier_name, size = rd.read_data(source_path, is_error_rate)
    f, p = stats.friedmanchisquare(*data.T)
    result = 'Begin ------------------------------\n' + result_template(classifier_name, size, confidence,
                                                                        'Friedman Test', f,
                                                                        p) + 'End --------------------------------\n'
    return result

# using example:
# if __name__ == '__main__':
#     one_way_variance('../../../dataset/evaluation/accuracy/avgAccuracy/part2_singleTrainTest.csv', False)
#
#     kruskal('../../../dataset/evaluation/accuracy/avgAccuracy/part2_singleTrainTest.csv', False)
#
#     friedman('../../../dataset/evaluation/accuracy/avgAccuracy/part2_singleTrainTest.csv', False)
