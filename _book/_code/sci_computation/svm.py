# -*- coding: utf-8 -*-

# @Time    : 2021/6/20 12:21
# @Author  : Zhongyu

import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score


def iris_label(s):
    it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return it[s]


# 数据读入
path = '../_data/iris/iris.data'
data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_label})
print(data.shape)

x, y = np.split(data, indices_or_sections=(4,), axis=1) #x为数据，y为标签
print(x.shape)
print(y.shape)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

# print(y_train.shape)
# print(x_train.shape)
# print(y_test.shape)
# print(x_test.shape)
#
# # 建模训练
# clf = svm.SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovr')  # ovr:一对多策略
# clf.fit(x_train, y_train.ravel())
#
#
# # 结果
# print("训练集：", clf.score(x_train, y_train))
# print("测试集：", clf.score(x_test, y_test))
#
# y_pred = clf.predict(x_test)
# y_test = y_test.ravel()
# print(y_pred)
# print(y_test)
# print(np.mean(y_pred == y_test))
#
# y_pred = clf.predict(x_test)
# print(accuracy_score(y_test, y_pred))
# print(precision_score(y_test, y_pred, average='macro'))
# print(recall_score(y_test, y_pred, average='macro'))


