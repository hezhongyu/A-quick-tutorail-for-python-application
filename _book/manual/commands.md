# 常用命令手册

介绍常用的python命令

## random
详见[官方文档](https://docs.python.org/zh-cn/3/library/random.html)

    # [0.0, 1.0) 之间均匀分布生成的随机浮点数
    random.random()

    # [a, b] 之间均匀分布生成的随机浮点数
    random.uniform(a, b)

    # 以mu为均值，sigma为标准差的高斯分布生成的随机浮点数，多线程慎用
    random.gauss(mu, sigma)

    # 生成[a, b] 之间的随机整数
    random.randint(a, b)

    # 生成[0, stop] 之间的随机整数
    random.randrange(stop)

    # 生成 range(start, stop[, step]) 之间的随机整数
    random.randrange(start, stop[, step])
    
    # 从非空序列 seq 返回一个随机元素
    random.choice(seq)

    # 从population中按照权值weights进行k次有放回随机抽取（cum_weights为累计权值，不常用），该功能 3.6 版本后才有
    random.choices(population, weights=None, *, cum_weights=None, k=1)

    # 从population中进行k次无放回随机抽取，counts为population的中元素的频数
    random.sample(population, k, *, counts=None)

    # 将序列 x 随机打乱位置
    random.shuffle(x)
    


