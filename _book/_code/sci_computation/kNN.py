# -*- coding: utf-8 -*-

# @Time    : 2021/6/20 10:34
# @Author  : Zhongyu

import numpy as np
from sklearn import neighbors
from sklearn.metrics import accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt


# 数据读入
train_data_path = '../_data/mnist/train-images.idx3-ubyte'
train_label_path = '../_data/mnist/train-labels.idx1-ubyte'
test_data_path = '../_data/mnist/t10k-images.idx3-ubyte'
test_label_path = '../_data/mnist/t10k-labels.idx1-ubyte'
y_train = np.fromfile(train_label_path, dtype=np.uint8)[8:]
x_train = np.fromfile(train_data_path, dtype=np.uint8)[16:].reshape(len(y_train), 784)
y_test = np.fromfile(test_label_path, dtype=np.uint8)[8:]
x_test = np.fromfile(test_data_path, dtype=np.uint8)[16:].reshape(len(y_test), 784)
print('数据载入完成')

# print(y_train.shape)
# print(x_train.shape)
# print(y_test.shape)
# print(x_test.shape)
#
y_train = y_train[:6000]
x_train = x_train[:6000]
y_test = y_test[:1000]
x_test = x_test[:1000]
#
# # 作图
# fig, ax = plt.subplots(
#     nrows=2,
#     ncols=5,)
#
# ax = ax.flatten()
# for i in range(10):
#     img = x_train[y_train == i][0].reshape(28, 28)
#     ax[i].imshow(img, cmap='Greys', interpolation='nearest')
#
# ax[0].set_xticks([])
# ax[0].set_yticks([])
# plt.tight_layout()
# plt.show()
#
# # 建模训练
# clf = neighbors.KNeighborsClassifier(algorithm='kd_tree')
# clf.fit(x_train, y_train)
# print('建模完成')
#
# # 结果
# print("训练集：", clf.score(x_train, y_train))
# print("测试集：", clf.score(x_test, y_test))
#
# y_pred = clf.predict(x_test)
# print(y_pred)
# print(y_test)
# print(np.mean(y_pred == y_test))
#
# print(accuracy_score(y_test, y_pred))
# print(precision_score(y_test, y_pred, average='macro'))
# print(recall_score(y_test, y_pred, average='macro'))

