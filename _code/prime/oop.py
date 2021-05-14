# -*- coding: utf-8 -*-

# @Time    : 2021/5/14 23:40
# @Author  : Zhongyu

import random


class Abel(object):
    def __init__(self, dna):
        """
        初始化
        :param dna: dna为一个100维的list
        """
        self.dna = dna
        self.viability = self.cal_viability()

    def propagate(self):
        new_creature = Abel(self.dna)
        return new_creature

    def mutate(self):
        position = random.randint(0, 99)
        choice = random.choice([1, -1])
        self.dna[position] = min(9, max(0, self.dna[position] + choice))
        self.survival = self.cal_survival()

    def cal_viability(self):
        return sum(self.dna)


creature_list = []
for i in range(200):
    dna = [0 for _ in range(100)]
    position = random.randint(0, 99)
    dna[position] = 1
    creature_list.append(Abel(dna))

env = 0
while env < 1000:
    # if env ==1:
    #     for creature in creature_list:
    #         print(creature.survival)
    # 环境恶化
    env += 1
    # 淘汰生物
    for s in range(len(creature_list)-1, -1, -1):
        if creature_list[s].survival < env:
            creature_list.pop(s)
    # 繁殖变异
    for i in range(len(creature_list)):
        new_creature = creature_list[i].propagate()
        new_creature.mutate()
        creature_list.append(new_creature)
    print(len(creature_list))
    print(env)
    if len(creature_list) == 0:
        break


for creature in creature_list:
    print(creature.survival)


