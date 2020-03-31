#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


test_names = ["Bob", "Jim", "Pam", "Michael"]
weights = np.array([1 for _ in range(len(test_names))])
weights[0] = 5
test_dict = dict(zip(test_names, weights))

picked = dict(zip(test_names, [0 for _ in range(len(test_names))]))
for i in range(1, 50):
    weights = np.array(list(test_dict.values()))
    norm_w = weights / sum(weights)
    draw = np.random.choice(list(test_dict.keys()), 1, p=norm_w)
    test_dict[draw[0]] = 1 / i
    picked[draw[0]] += 1
    # print(draw, norm_w)

test_dict = dict(zip(test_names, norm_w))

print(test_dict)
print(picked)

"""
[0, 0, 0, 0]
[1, 0, 0, 0]
[1, 1, 0, 0]
[2, 1, 0, 1]
"""
