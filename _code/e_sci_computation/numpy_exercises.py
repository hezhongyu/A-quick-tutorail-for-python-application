# -*- coding: utf-8 -*-

# @Time    : 2021/5/30 23:01
# @Author  : Zhongyu

import numpy as np


# z-score 标准化
x = np.arange(10)
print((x - x.mean()) / x.std())

# RMSE
y = np.arange(10)
y_hat = np.ones(10)
mae = np.sqrt((1 / y.size) * np.sum(np.square(y_hat - y)))
print(mae)
