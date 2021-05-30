# 常用命令手册

介绍常用的python命令

## random
Python内建库，详见[官方文档](https://docs.python.org/zh-cn/3/library/random.html)

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
    

## uuid
Python内建库，详见[官方文档](https://docs.python.org/zh-cn/3/library/random.html)

    # 基于MAC地址，时间戳，随机数来生成唯一的uuid
    uuid.uuid1()

    # 通过计算一个命名空间和名字的md5散列值来给出一个uuid。其中namespace参数是在uuid模块中本身给出的一些值，如uuid.NAMESPACE_DNS、uuid.NAMESPACE_OID、uuid.NAMESPACE_OID这些值，这些值本身也是UUID对象。
    uuid.uuid3(namespace,name)

    # 通过伪随机数得到uuid
    uuid.uuid4()

    # 和uuid3基本相同，只不过采用的散列算法是sha1
    uuid.uuid5(namespace,name）

> Python的`uuid`模块中没有`uuid2()`方法。
