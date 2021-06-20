# -*- coding: utf-8 -*-

# @Time    : 2021/5/30 22:18
# @Author  : Zhongyu

import random


class Abel(object):
    def __init__(self, dna):
        """
        初始化
        :param dna: dna为一个100维的list
        """
        self.dna = dna
        self.survival = self._cal_survival()

    def propagate(self):
        """
        繁殖方法
        :return: 新繁殖的个体
        """
        new_abel = Abel(self.dna)
        new_abel._mutate()
        return new_abel

    def _mutate(self):
        """
        变异方法，外部不能调用
        :return:
        """
        position = random.randint(0, 99)
        choice = random.choice([1, -1])
        self.dna[position] = min(9, max(0, self.dna[position] + choice))
        self.survival = self._cal_survival()
        return

    def _cal_survival(self):
        """
        计算个体的生存能力方法，外部不能调用
        :return: 该实例的生存能力
        """
        return sum(self.dna)


def eliminate(creature_list, env):
    """
    淘汰方法
    :param creature_list: 所有个体实例组成的列表
    :param env: 外部环境
    :return: 淘汰完后剩余的个体实例组成的列表
    """
    # 环境淘汰
    for s in range(len(creature_list)-1, -1, -1):
        if creature_list[s].survival < env:
            creature_list.pop(s)
    # 种群数量淘汰
    creature_list.sort(key=lambda _i: _i.survival, reverse=True)
    if len(creature_list) > 1000:
        creature_list = creature_list[:1000]
    return creature_list


########### 主要运行，程序入口 ############

# 初始Abel的种群与环境
abel_list = []
for i in range(100):
    dna = [0 for _ in range(100)]
    abel_list.append(Abel(dna))
env = 0

# 环境不断恶化，开始优胜劣汰
while True:
    # 繁殖变异
    for i in range(len(abel_list)):
        new_creature = abel_list[i].propagate()
        abel_list.append(new_creature)

    # 淘汰
    abel_list = eliminate(abel_list, env)

    env += 1
    # 当没有个体生存了，跳出循环
    if len(abel_list) == 0:
        break

    print(env, len(abel_list))
    print(abel_list[0].dna)

