#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


def init_weight(name_arr:np.array) -> np.array:
    return 1 / len(name_arr)
def init_count(count_arr:np.array, events=1000) -> np.array:
    return np.array([events for _ in range(len(count_arr))])
def norm_weight(count_arr:np.array) -> np.array:
    return count_arr / sum(count_arr)

names = ["Bob", "Jim", "Pam", "Michael", "Dwight"]
counts = init_count(names)

class_df = pd.DataFrame({
        "Name" : names,
        "Count" : counts,
        "Weight" : init_weight(names)
        }
)



draw = np.random.choice(class_df["Name"], 1, p=class_df["Weight"])
print(class_df.loc[class_df['Name'] == draw[0]])
d_idx = class_df.index[class_df["Name"] == draw[0]]
class_df[d_idx].at["Count"] -= 1
print(draw)
print(class_df.loc[class_df['Name'] == draw[0]])

# print(class_df)

"""
[0, 0, 0, 0]
[1, 0, 0, 0]
[1, 1, 0, 0]
[2, 1, 0, 1]
"""
