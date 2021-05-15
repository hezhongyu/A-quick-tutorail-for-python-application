# 文件与IO

## 控制台
### 输出
以下代码输出到控制台：

    print('Nice python!')
    print('学Python真开心!')

若输出中文遇到乱码问题，通常情况下是编码问题。

### 输入

    a = input()
    print("您输入的是" + a)

    b = float(input("请您输入:"))
    print("您输入的是" + b)


## 编码
- ASCII  
    0x00~0x7f   
- ANCI  
    0x80~0xFFFF 比如：汉字 '中' 在中文操作系统中，使用 [0xD6,0xD0] 这两个字节存储。  
- gbk   
    不同的国家和地区制定了不同的标准，由此产生了 GB2312、GBK、GB18030、Big5、Shift_JIS 等各自的编码标准。这些使用多个字节来代表一个字符的各种汉字延伸编码方式，称为 ANSI 编码。在简体中文Windows操作系统中，ANSI 编码代表 GB2312编码；在繁体中文Windows操作系统中，ANSI编码代表Big5；在日文Windows操作系统中，ANSI 编码代表 JIS 编码。
- Unicode
    Unicode用数字0-0x10FFFF来映射这些字符，最多可以容纳1114112个字符，或者说有1114112个码位。
- utf-8
    UTF-8、UTF-16（UTF后的数字代表编码的最小单位，如UTF-8表示最小单位1字节（=8 bits）,所以它可以使用1、2、3、4字节等进行编码，UTF-16表示最小单位2字节，所以它可以使用2、4字节进行编码）都是Unicode的编码方案。其中UTF-8因可以兼容ASCII而被广泛使用。
    UTF-8使用1~4字节为每个字符编码：
    ·一个US-ASCIl字符只需1字节编码（Unicode范围由U+0000~U+007F）。
    ·带有变音符号的拉丁文、希腊文、西里尔字母、亚美尼亚语、希伯来文、阿拉伯文、叙利亚文等字母则需要2字节编码（Unicode范围由U+0080~U+07FF）。
    ·其他语言的字符（包括中日韩文字、东南亚文字、中东文字等）包含了大部分常用字，使用3字节编码。
    ·其他极少使用的语言字符使用4字节编码。

## 路径
相对路径与绝对路径
- 相对路径
    
        # 我们现在的位置在'C:/code/A-quick-tutorail-for-python-application/_code'
        path = '/data/iris.data'
    
        # 我们现在的位置在'C:/code/A-quick-tutorail-for-python-application/_code/cook'
        path = '../data/iris.data' 

- 绝对路径

        path = 'C:/code/A-quick-tutorail-for-python-application/_code/data/iris.data'


## txt
.txt是包含极少格式信息的文字文件的扩展名。.txt格式并没有明确的定义，它通常是指那些能够被系统终端或者简单的文本编辑器接受的格式。任何能读取文字的程序都能读取带有.txt扩展名的文件，因此，通常认为这种文件是通用的、跨平台的。  
在英文文本文件中，ASCII字符集是最为常见的格式，而且在许多场合，它也是默认的格式。对于带重音符号的和其它的非ASCII字符，必须选择一种字符编码。在很多系统中，字符编码是由计算机的区域设置决定的。常见的字符编码包括支持许多欧洲语言的ISO 8859-1。  
由于许多编码只能表达有限的字符，通常它们只能用于表达几种语言。Unicode制定了一种试图能够表达所有已知语言的标准，Unicode字符集非常大，它囊括了大多数已知的字符集。Unicode有多种字符编码，其中最常见的是UTF-8，这种编码能够向后兼容ASCII，相同内容的ASCII文本文件和UTF-8文本文件完全一致。

### txt读取

读取全部内容

    f = open("test.txt") 
    data = f.read()  # 读取文件
    print(data)


    with open("test.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        print(data)

读取第一行内容

    with open("test.txt", "r") as f:
        data = f.readline()
        print(data)

读取全部内容，以数列格式返回结果

    with open("test.txt", "r") as f:
        data = f.readlines()
        print(data)

    with open("test.txt", "r") as f:
        for line in f.readlines():
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            print(line)


### txt写入

    with open("test.txt","w") as f:
        f.write("这是个测试！")  # 自带文件关闭功能，不需要再写f.close()


## csv
逗号分隔值（Comma-Separated Values，CSV，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。纯文本意味着该文件是一个字符序列，不含必须像二进制数字那样被解读的数据。CSV文件由任意数目的记录组成，记录间以某种换行符分隔；每条记录由字段组成，字段间的分隔符是其它字符或字符串，最常见的是逗号或制表符。通常，所有记录都有完全相同的字段序列。通常都是纯文本文件。

以下的csv文件的读写均需要先引入python标准库提供的csv模块：

    import csv


### csv读取

以下两种写法皆可

    # 第一种写法
    f = open(path, 'r')
    f_reader = csv.reader(f)
    for i in f_reader:
        print(i)
    f.close()

    # 第二种写法
    with open(path)as f:
        f_reader = csv.reader(f)
        for row in f_reader:
            print(row)

### csv写入

以下两种写法皆可：

    # 第一种写法
    f = open(path, 'w')
    f_writer = csv.writer(f)
    for i in data:
        writer.writerow(i)
    f.close()

    # 第二种写法
    with open(path,'w',newline='')as f:
        f_csv = csv.DictWriter(f,headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

> 读者可以试一试在第二种写法中不加`newline=''`会输出什么。


## json
JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。它基于 ECMAScript (欧洲计算机协会制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

1. “名称/值”对的集合（A collection of name/value pairs）

不同的编程语言中，它被理解为对象（object），纪录（record），结构（struct），字典（dictionary），哈希表（hash table），有键列表（keyed list），或者关联数组 （associative array）。

2. 值的有序列表（An ordered list of values）。

在大部分语言中，它被实现为数组（array），矢量（vector），列表（list），序列（sequence）。

这些都是常见的数据结构。目前，大部分编程语言都支持它们。这使得在各种编程语言之间交换同样格式的数据成为可能。

    {
        "title": "Composer Library",
        "description": "This is a composer library",
        "composer number": 3
        "composers": [
            {
                "id": 1,
                "name": "Bach",
                "nationality": "Germany" ,
                "works":[
                    {
                        "name": "Toccata and Fugue in D minor",
                        "number": "BWV 565"
                    },
                    {
                        "name": "Brandenburg Concertos",
                        "number": "BWV 1046-1051"
                    }
                ]
            },
            {
                "id": 2,
                "name": "Mozart",
                "nationality": "Austrian" 
            },
            {
                "id": 3,
                "name": "Beethoven",
                "nationality": "Germany" 
            },
        ]
    }

以下的json文件的读写均需要先引入python标准库提供的json模块：

    import json


### json读取

从文件中读取

    with open(path,'r') as load_f:
        load_dict = json.load(load_f)

从字符串中读取

    new_dict = json.loads(json_str)


### json写入

写入到文件中

    with open(path,"w") as f:
        json.dump(new_dict,f)


写入到字符串中

    json_str = json.dumps(test_dict)


## 其他常用格式
- html：
- mat:

## 作业
1. 通过文本方式读取Iris数据集。
    1. 定义一个`Iris`类，并实例化每一朵Iris，使它具有数据集中的实例属性。同时在该类下定义一种方法：`iris_print()`，实现向控制台输出此朵Iris各种属性的功能。
    2. 将所有`Iris`实例存在一个列表中，循环此列表调用`iris_print()`方法。
    3. 还原一个csv格式输出。

2. Math星球墓志铭。
