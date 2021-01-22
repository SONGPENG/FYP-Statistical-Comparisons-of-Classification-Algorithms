# -*- coding: utf-8 -*-
"""
@File  : statisticsMethod2.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/11 14:11
@Desc  : 
"""

import scipy.stats as stats
import hypothesisTesting.readData as rd
import pandas as pd


def result_template(classifier_name, size, confidence, name, s, p):
    """

    :param classifier_name:
    :param size:
    :param confidence:
    :param name:
    :param s:
    :param p:
    :return:
    """
    result = 'Program to analyze Performance between ' + classifier_name[0] + ' and ' + classifier_name[
        1] + ' using ' + name + '.'
    result += '\n\nNumber of test point: ' + str(size)
    result += '\nConfidence level: ' + str(confidence)
    result += '\nStatistics: ' + str(round(s, 2)) + ',  P value: ' + str(round(p, 4))
    if p < confidence:
        result += '\n\nP value < Confidence,\nNull Hypothesis rejected.\n'
    else:
        result += '\n\nP value > Confidence,\nNull Hypothesis accepted.\n'
    return result


def rank_sums(source_path, is_error_rate, confidence=0.05):
    """
    Nonparametric method.
    better performance: when size < 20 and independent sample.

    @param source_path:
    @param is_error_rate:
    @param confidence:
    @return:
    """
    data, classifier_name, size = rd.read_data(source_path, is_error_rate)
    r, p = stats.wilcoxon(data[:, 0], data[:, 1])
    result = 'Begin ------------------------------\n' + result_template(classifier_name, size, confidence,
                                                                        'Rank Sums', r,
                                                                        p) + 'End --------------------------------\n'

    return result


def mannwhitneyu(source_path, is_error_rate, confidence=0.05, use_continuity=True, alternative=None):
    """
    Nonparametric method.
    better performance: U test, when size > 20 and independent sample, better than Rank Sums.

    @param source_path:
    @param is_error_rate:
    @param confidence:
    @param use_continuity: bool, optional.
    Whether a continuity correction (1/2.) should be taken into account.
    Default is True.
    @param alternative: {None, 'two-sided', 'less', 'greater'}, optional.
    Defines the alternative hypothesis.
    The following options are available (default is None):
        *   None: computes p-value half the size of the ‘two-sided’ p-value and a different U statistic. The default behavior is not the same as using ‘less’ or ‘greater’; it only exists for backward compatibility and is deprecated.
        *   'two-sided'
        *   'less': one-sided
        *   'greater': one-sided
    @return:
    """
    data, classifier_name, size = rd.read_data(source_path, is_error_rate)
    m, p = stats.mannwhitneyu(data[:, 0], data[:, 1], use_continuity, alternative)

    result = 'Begin ------------------------------\n' + result_template(classifier_name, size, confidence,
                                                                        'Mann-Whitneyu', m,
                                                                        p) + 'End --------------------------------\n'

    return result


def wilcoxon(source_path, is_error_rate, confidence=0.05, zero_method='wilcox', correction=False,
             alternative='two-sided'):
    """
    Nonparametric method, paired data.

    @param source_path:
    @param is_error_rate:
    @param confidence:
    @param zero_method: {'pratt', 'wilcox', 'zsplit'}, optional.
    The following options are available (default is 'wilcox'):
        *   'pratt': Includes zero-differences in the ranking process, but drops the ranks of the zeros, see [4], (more conservative).
        *   'wilcox’: Discards all zero-differences, the default.
        *   'zsplit’: Includes zero-differences in the ranking process and split the zero rank between positive and negative ones.
    @param correction: bool, optional
    If True, apply continuity correction by adjusting the Wilcoxon rank statistic by 0.5 towards
        the mean value when computing the z-statistic. Default is False.
    @param alternative: {'two-sided', 'greater', 'less'}, optional.
    The alternative hypothesis to be tested, see Notes. Default is “two-sided”.
    @return:
    """

    data, classifier_name, size = rd.read_data(source_path, is_error_rate)
    print(data[:, 0], data[:, 1])

    w, p = stats.wilcoxon(data[:, 0], data[:, 1], zero_method, correction, alternative)

    result = 'Begin ------------------------------\n' + result_template(classifier_name, size, confidence, 'Wilcoxon',
                                                                        w, p) + 'End --------------------------------\n'

    return result


def ttest(source_path, is_error_rate, confidence=0.05, nan_policy='propagate'):
    """
    Parameter method.

    @param source_path:
    @param is_error_rate:
    @param confidence:
    @param nan_policy: {'propagate', 'raise', 'omit'}, optional.
    Defines how to handle when input contains nan. The following options are available. default is 'propagate':
        *   'propagate': returns nan.
        *   'raise': throws an error.
        *   'omit;: performs the calculations ignoring nan values.
    @return:
    """
    data, classifier_name, size = rd.read_data(source_path, is_error_rate)
    print(data[:, 0], data[:, 1])

    t, p = stats.ttest_rel(data[:, 0], data[:, 1])

    result = 'Begin ------------------------------\n' + result_template(classifier_name, size, confidence,
                                                                        'Paired T test', t,
                                                                        p) + 'End --------------------------------\n'

    return result


def mc_nemar(source_path, confidence=0.05, ):
    """
    Nonparametric Method
    McNemar Test, Paired data.
    @param source_path:
    @param confidence:
    @return:
    """

    df = pd.read_csv(source_path, index_col=0, header=0)
    data = df.values.T
    classifier_name = df.axes[1].tolist()
    k, p, _, _ = stats.chi2_contingency(data)

    result = 'Begin ------------------------------\n' + 'Program to analyze Performance between ' + classifier_name[
        0] + ' and ' + \
             classifier_name[
                 1] + ' using McNemar'
    result += '\n\nConfidence level: ' + str(confidence)
    result += '\nStatistics: ' + str(round(k, 2)) + ',  P value: ' + str(round(p, 4))
    if p < confidence:
        result += '\n\nP value < Confidence, Null Hypothesis rejected.\n'
    else:
        result += '\n\nP value > Confidence, Null Hypothesis accepted.\n'
    result += 'End --------------------------------\n'

    return result

# using examples:
# if __name__ == '__main__':
#     rank_sums('../../../dataset/evaluation/accuracy/avgAccuracy/part1_singleTrainTest.csv', False, confidence=0.05)
#
#     wilcoxon('../../../dataset/evaluation/accuracy/avgAccuracy/part1_singleTrainTest.csv', False, confidence=0.05,
#              zero_method='wilcox', correction=False, alternative='two-sided')
#
#     ttest('../../../dataset/evaluation/accuracy/avgAccuracy/part1_singleTrainTest.csv', False, confidence=0.05)
#
#     mannwhitneyu('../../../dataset/evaluation/accuracy/avgAccuracy/part1_singleTrainTest.csv', False, confidence=0.05)
#
#     mc_nemar('../../../dataset/evaluation/crosstabs/test.csv')
