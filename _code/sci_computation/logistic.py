# -*- coding: utf-8 -*-

# @Time    : 2021/6/20 13:25
# @Author  : Zhongyu


import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = load_boston().data
print(data.shape)

x, y = np.split(data, indices_or_sections=(12,), axis=1)
print(x.shape)
print(y.shape)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

print(y_train.shape)
print(x_train.shape)
print(y_test.shape)
print(x_test.shape)

# 建模
model = LinearRegression()
model.fit(x_train, y_train)

print(model.predict(x_test))
print("训练集：", model.score(x_train, y_train))
print("测试集：", model.score(x_test, y_test))




