# numpy

NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

NumPy 的前身 Numeric 最早是由 Jim Hugunin 与其它协作者共同开发，2005 年，Travis Oliphant 在 Numeric 中结合了另一个同性质的程序库 Numarray 的特色，并加入了其它扩展而开发了 NumPy。NumPy 为开放源代码并且由许多协作者共同维护开发。

NumPy 是一个运行速度非常快的数学库，主要用于数组计算，包含：

一个强大的N维数组对象 ndarray
广播功能函数
整合 C/C++/Fortran 代码的工具
线性代数、傅里叶变换、随机数生成等功能

## NumPy 应用
NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用， 这种组合广泛用于替代 MatLab，是一个强大的科学计算环境，有助于我们通过 Python 学习数据科学或者机器学习。

SciPy 是一个开源的 Python 算法库和数学工具包。

SciPy 包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算。

Matplotlib 是 Python 编程语言及其数值数学扩展包 NumPy 的可视化操作界面。它为利用通用的图形用户界面工具包，如 Tkinter, wxPython, Qt 或 GTK+ 向应用程序嵌入式绘图提供了应用程序接口（API）。

## 安装
Numpy不是Python标准库，而是第三方库，所以需要安装。  
若你是通过Anaconda进行安装的，则自带了numpy库。
若您需要安装numpy，可以通过pip进行安装：

    pip install numpy

以下所有默认已经引入了该包

    import numpy as np


## NumPy Ndarray 对象
NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。

ndarray 对象是用于存放同类型元素的多维数组。

ndarray 中的每个元素在内存中都有相同存储大小的区域。

ndarray 内部由以下内容组成：

一个指向数据（内存或内存映射文件中的一块数据）的指针。

数据类型或 dtype，描述在数组中的固定大小值的格子。

一个表示数组形状（shape）的元组，表示各维度大小的元组。

一个跨度元组（stride），其中的整数指的是为了前进到当前维度下一个元素需要"跨过"的字节数。

ndarray 的内部结构:
![结构图](../images/numpy/ndarray.png)

    a = np.array([1,2,3])  
    print (a)

    # 多于一个维度  
    a = np.array([[1,  2],  [3,  4]])  
    print (a)

    # 最小维度  
    a = np.array([1,  2,  3,4,5], ndmin =  2)  
    print (a)

    # dtype 参数  
    a = np.array([1,  2,  3], dtype = complex)  
    print (a)


## numpy数据类型

numpy 支持的数据类型比 Python 内置的类型要多很多，基本上可以和 C 语言的数据类型对应上，其中部分类型对应为 Python 内置的类型。下表列举了常用 NumPy 基本类型。

名称	描述  
bool_	布尔型数据类型（True 或者 False）  
int_	默认的整数类型（类似于 C 语言中的 long，int32 或 int64）  
intc	与 C 的 int 类型一样，一般是 int32 或 int 64  
intp	用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）  
int8	字节（-128 to 127）  
int16	整数（-32768 to 32767）  
int32	整数（-2147483648 to 2147483647）  
int64	整数（-9223372036854775808 to 9223372036854775807）  
uint8	无符号整数（0 to 255）  
uint16	无符号整数（0 to 65535）  
uint32	无符号整数（0 to 4294967295）  
uint64	无符号整数（0 to 18446744073709551615）  
float_	float64 类型的简写  
float16	半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位  
float32	单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位  
float64	双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位  
complex_	complex128 类型的简写，即 128 位复数  
complex64	复数，表示双 32 位浮点数（实数部分和虚数部分）  
complex128	复数，表示双 64 位浮点数（实数部分和虚数部分）  

## 初始化

### 创建数组
- numpy.empty

    numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：

        numpy.empty(shape, dtype = float, order = 'C')

    举例

        x = np.empty([3,2], dtype = int) 
        print (x)

    > 数组元素为随机值，因为它们未初始化。

- numpy.zeros

    创建指定大小的数组，数组元素以 0 来填充：

        numpy.zeros(shape, dtype = float, order = 'C')

    举例
    
        # 默认为浮点数
        x = np.zeros(5) 
        print(x)
        
        # 设置类型为整数
        y = np.zeros((5,), dtype = np.int) 
        print(y)
        
        # 自定义类型
        z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
        print(z)

- numpy.ones

    创建指定形状的数组，数组元素以 1 来填充：

        numpy.ones(shape, dtype = None, order = 'C')

    举例
 
        # 默认为浮点数
        x = np.ones(5) 
        print(x)
        
        # 自定义类型
        x = np.ones([2,2], dtype = int)
        print(x)

### 从已有数组中创建数组
- numpy.array

        # 列表
        x =  [1,2,3] 
        a = np.asarray(x)  
        print (a)

        # 元组
        x =  (1,2,3) 
        a = np.asarray(x)  
        print (a)

        # 元组列表
        x =  [(1,2,3),(4,5)] 
        a = np.asarray(x)  
        print (a)

        # 设置参数
        x =  [1,2,3] 
        a = np.asarray(x, dtype=float)  
        print (a)

- numpy.asarray

- array与asarray区别

    array和asarray都可以将结构数据转化为ndarray，但是主要区别就是当数据源是ndarray时，array仍然会copy出一个副本，占用新的内存，但asarray不会。

        #example 1: 
        data1=[[1,1,1],[1,1,1],[1,1,1]] 
        arr2=np.array(data1) 
        arr3=np.asarray(data1) 
        data1[1][1]=2 
        print('data1:\n',data1)
        print('arr2:\n',arr2)
        print('arr3:\n',arr3)

    可见array和asarray没有区别，都对元数据进行了复制。

        #example 2: 
        arr1=np.ones((3,3)) 
        arr2=np.array(arr1) 
        arr3=np.asarray(arr1) 
        arr1[1]=2 
        print('arr1:\n',arr1)
        print('arr2:\n',arr2)
        print('arr3:\n',arr3)

    此时两者才表现出区别

### 从数值范围创建数组
- numpy.arange

        x = np.arange(5)  
        print (x)

        x = np.arange(10,20,2)  
        print (x)


- numpy.linspace

        x = np.linespace(10,20,5)  
        print (x)

- 区别

    1、arange(初始值，结束值，间隔) 生成的序列不包含结束值，linspace(初始值, 结束值, 值的个数) 生成的序列包含结束值。

    2、如果要使 linspace 和 arrange 等效，可以用 linspace(初始值, 结束值, 值的个数, endpoint = False). 当然，两者有各自的使用场景，尽量不要混用。arrange 适用于知道序列中相邻两数之间的间隔的情况下，比如生成一定范围内奇数或者偶数的序列。linspace 适合序列长度和序列取值范围已知的情况。比如采样频率为1200 Hz, 也就是说 0~1s 之间有1200 个点。

### 从文件读取

Numpy 可以读写磁盘上的文本数据或二进制数据。  
NumPy 为 ndarray 对象引入了一个简单的文件格式：npy。  
npy 文件用于存储重建 ndarray 所需的数据、图形、dtype 和其他信息。

- from_file(), to_file()

        a = np.arange(100).reshape(5,10,2)
        a.tofile('b.dat',sep=',',format='%d')
        c = np.fromfile('b.dat', dtype=np.int, sep=',')
        print(c)

    尽量不要使用fromfile()和tofile()因为其具有平台依赖性，没有存储与字节顺序和字节类型相关的信息。可以使用save()和load()将文件存储为.npy格式，进行平台独立行存储

- load(), save(), savez()
    函数将数组保存到以 .npy 为扩展名的文件中。

    举例：
    
        a = np.array([1,2,3,4,5]) 
        
        # 保存到 outfile.npy 文件上
        np.save('outfile.npy',a) 
        
        # 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
        np.save('outfile2',a)

        # 读取
        b = np.load('outfile.npy')
        print(b)

    numpy.savez() 函数将多个数组保存到以 npz 为扩展名的文件中。

    举例：
    
        a = np.array([[1,2,3],[4,5,6]])
        b = np.arange(0, 1.0, 0.1)
        c = np.sin(b)
        # c 使用了关键字参数 sin_array
        np.savez("runoob.npz", a, b, sin_array = c)
        r = np.load("runoob.npz")  
        print(r.files) # 查看各个数组名称
        print(r["arr_0"]) # 数组 a
        print(r["arr_1"]) # 数组 b
        print(r["sin_array"]) # 数组 c

- loadtxt(), savetxt()
    savetxt() 函数是以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据。

        np.loadtxt(FILENAME, dtype=int, delimiter=' ')
        np.savetxt(FILENAME, a, fmt="%d", delimiter=",")

    举例：
        
        a = np.array([1,2,3,4,5]) 
        np.savetxt('out.txt',a) 
        b = np.loadtxt('out.txt')  
        
        print(b)

    使用 delimiter 参数：
 
        a=np.arange(0,10,0.5).reshape(4,-1)
        np.savetxt("out.txt",a,fmt="%d",delimiter=",") # 改为保存为整数，以逗号分隔
        b = np.loadtxt("out.txt",delimiter=",") # load 时也要指定为逗号分隔
        print(b)


- genfromtxt

        c = np.genfromtxt('out.txt', dtype=np.init, delimiter=',')
        print(c)

