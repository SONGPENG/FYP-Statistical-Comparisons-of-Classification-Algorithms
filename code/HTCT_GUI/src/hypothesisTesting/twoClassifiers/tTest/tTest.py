# -*- coding: utf-8 -*-
"""
@File  : test.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/9 22:59
@Desc  :
"""

import matlab.engine
import matlab


def t_test(perf_classifier_a, perf_classifier_b, nb_test_points, confidence=0.05):
    eng = matlab.engine.start_matlab()
    result = eng.classifier_performance_ttest(perf_classifier_a, perf_classifier_b, float(nb_test_points), confidence)
    eng.exit()
    return result


# example
result = t_test(0.533, 0.300, 30)
