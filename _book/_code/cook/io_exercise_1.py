# -*- coding: utf-8 -*-

# @Time    : 2021/5/15 3:45
# @Author  : Zhongyu

import csv


class Iris(object):
    def __init__(self, row):
        self.sepal_length = row[0]
        self.sepal_width = row[1]
        self.petal_length = row[2]
        self.petal_width = row[3]
        self.iris_class = row[4]

    def iris_print(self):
        print('这朵花长{}, 宽{}，种类为{}'.format(self.sepal_length, self.sepal_width, self.iris_class))


path = '_data/iris.data'

iris_list = []
# 读取csv
with open(path)as f:
    f_reader = csv.reader(f)
    for row in f_reader:
        if len(row) > 0:
            # 初始化每一朵花并加入列表
            iris_list.append(Iris(row))

for iris in iris_list:
    iris.iris_print()
