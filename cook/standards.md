# 代码规范

良好的代码规范是每个程序员所需要遵守的。

- 代码可读性提升。自己始终用一种代码规范，可以让未来的自己更能看懂自己的代码。
- 一个团队成员用一种代码规范，可以使得大家的沟通成本降低，也易于项目的维护。

[PEP8](https://www.python.org/dev/peps/pep-0008/)
以下规范大部分为PEP8所规定的代码规范，又结合了少量编者自己的习惯。读者若是觉得其中某些地方不合理或者不喜欢，也可以在不影响程序运行的前提下，自己定义一套代码规范，只是编者不建议这么做 :P。

## 命名

python库的命名一直很乱，没有做到统一，但现在有一些推荐的命名规范，新的一些包会采用这个规则。当然你可以不采用这一规则，但请在自己的代码中保持自己的风格，而不要混合使用一些命名规则，当涉及到多人合作时，也请和合作者商量好运用同一种命名规则。

### 必须遵守

- 变量名可以包括字母、数字、下划线，但是数字不能做为开头。例如：name1是合法变量名，而1name就不可以。
- 系统关键字不能做变量名使用
- Python的变量名是区分大小写的

### 最高标准
暴露给用户的API，应该以实现环境为标准进行命名，而不是以内部实现过程的标准进行命名。

1. 包名与模块名  
包名与模块名应为简单的、全小写的字母，如`package`、`module`。对于模块名，若为了提高可读性，可在名字中加入下划线，如`my_module`；对于包名，则不建议这么做。  
若模块是由C或C++编写的更高级别的接口（具体做法见“混合编程”部分），则该模块名字需要有个前置的下划线，如`_socket`。

2. 类名  
首字母大写，以一个或少量单词组成，如`Dog`。如需要多个单词，使用驼峰命名法（Pascal命名法），如`MyDog`。

3. 函数名与变量名  
函数名与变量名的命名规则一致，由全部小写字母进行命名，若为了提高可读性，可在其中加入下划线。  
若函数和变量是在类中所定义的，那么命名规则与以上一致，但也有特殊的命名方式在以下提到。

4. 类或实例中的方法名与变量名
类或实例中的方法和变量的命名规则与一般的函数与变量相同，都是由由全部小写字母进行命名，若为了提高可读性，可在其中加入下划线。  
但不同的是，在类的定义中，我们可以通过在变量名前加上下划线的方式表明变量的访问级别。

    Use one leading underscore only for non-public methods and instance variables.

    To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

    Python mangles these names with the class name: if class Foo has an attribute named __a, it cannot be accessed by Foo.__a. (An insistent user could still gain access by calling Foo._Foo__a.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.

    Note: there is some controversy about the use of __names (see below).

    > 此处命名例如`name`、`_name`、`__name`的方式，与传统的静态语言（如C/C++/Java等）中的访问修饰符`public`、`protected`、`private`有些类似，但最大的不同是，Python中命名方式只是提供了阅读上的便利，非强制性，就算你在变量名之前加了下划线，表明了该变量的访问级别，你仍可以在外部进行调用。

5. 常量名
常量通常定义在“模块”这一级别，由全部的大写字母与下划线组成，例如`MAX_OVERFLOW`、`TOTAL`。

6. 异常名
由于异常通常都作为类进行定义，所以类的命名方式适用于此。同时，若你所定义的异常类确实是一个“异常”，那么应该在命名中使用后缀“Error”。

7. 全局变量名

(Let's hope that these variables are meant for use inside one module only.) The conventions are about the same as those for functions.

Modules that are designed for use via `from M import *` should use the `__all__` mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are "module non-public").

> `__all__`的用法，参考[链接](http://c.biancheng.net/view/2401.html)。

其他需要注意的有：
- 应避免的名字：  
建议不要使用字母‘l’（小写的L），‘O’（大写的O），或者‘I’（大写的I）作为单字符变量名。原因显而易见，在有些字体里，这些字符无法和数字0和1区分
- 应避免的符号：
建议在所有命名中都不要使用`-`符号，尽量使用`_`作为命名的分隔符。
- 前后带有下划线的变量：
    - `_single_leading_underscore`：（单下划线开头）弱“内部使用”指示器。比如 from M import * 是不会导入以下划线开始的对象的。
    - `single_trailing_underscore_`：（单下划线结尾）这是避免和Python内部关键词冲突的一种约定，比如：Tkinter.Toplevel(master, class_=’ClassName’)
    - `__double_leading_underscore`：（双下划线开头）当这样命名一个类的属性时，调用它的时候名字会做矫正（在类FooBar中，__boo变成了_FooBar__boo；见下文）。
    - `__double_leading_and_trailing_underscore__`：（双下划线开头，双下划线结尾）“magic”对象或者存在于用户控制的命名空间内的属性，例如：`__init__`,`__import__`或者`__file__`。除了作为文档之外，永远不要命这样的名。


4. 类中的形式参数
永远将`self`作为实例方法的第一个参数，永远将`cls`作为该类的静态方法的第一个参数。


## 布局排版

### 缩进
- 每一级缩进使用4个空格。

续行应该与其包裹元素对齐，要么使用圆括号、方括号和花括号内的隐式行连接来垂直对齐，要么使用挂行缩进对齐3。当使用挂行缩进时，应该考虑到第一行不应该有参数，以及使用缩进以区分自己是续行。

- 制表符还是空格？
    - PEP8所述：空格是首选的缩进方式。但在实际工作中，通常制表符会更方便省力（特别是有IDE的帮助）。
    - 制表符只能用于与同样使用制表符缩进的代码保持一致。
    - Python3不允许同时使用空格和制表符的缩进。


### 行的最大长度
所有行限制的最大字符数为79。

没有结构化限制的大块文本（文档字符或者注释），每行的最大字符数限制在72。

限制编辑器窗口宽度可以使多个文件并行打开，并且在使用代码检查工具(在相邻列中显示这两个版本)时工作得很好。
大多数工具中的默认封装破坏了代码的可视化结构，使代码更难以理解。避免使用编辑器中默认配置的80窗口宽度，即使工具在帮你折行时在最后一列放了一个标记符。某些基于Web的工具可能根本不提供动态折行。
较长的代码行选择Python在小括号，中括号以及大括号中的隐式续行方式。通过小括号内表达式的换行方式将长串折成多行。这种方式应该优先使用，而不是使用反斜杠续行。
反斜杠有时依然很有用。比如，比较长的，多个with状态语句，不能使用隐式续行，所以反斜杠是可以接受的：

    with open('/path/to/some/file/you/want/to/read') as file_1, \
        open('/path/to/some/file/being/written', 'w') as file_2:
        file_2.write(file_1.read())
（请参阅前面关于多行if-语句的讨论，以获得关于这种多行with-语句缩进的进一步想法。） 

另一种类似情况是使用assert语句。
确保在续行进行适当的缩进。


### 空行
顶层函数和类的定义，前后用两个空行隔开。
类里的方法定义用一个空行隔开。
相关的功能组可以用额外的空行隔开，在函数中使用空行来区分逻辑段。


### Imports 导入
导入通常在分开的行，例如：

推荐: 

    import os
    import sys

不推荐:

    import sys, os

也可以：

    from subprocess import Popen, PIPE

导入总是位于文件的顶部，在模块注释和文档字符串之后，在模块的全局变量与常量之前。  
导入应该按照以下顺序分组：

- 标准库导入
- 相关第三方库导入
- 本地应用/库特定导入

你应该在每一组导入之间加入空行。

推荐使用绝对路径导入，如果导入系统没有正确的配置（比如包里的一个目录在sys.path里的路径后），使用绝对路径会更加可读并且性能更好（至少能提供更好的错误信息）:

    import mypkg.sibling
    from mypkg import sibling
    from mypkg.sibling import example

然而，显示的指定相对导入路径是使用绝对路径的一个可接受的替代方案，特别是在处理使用绝对路径导入不必要冗长的复杂包布局时：

    from . import sibling
    from .sibling import example

标准库要避免使用复杂的包引入结构，而总是使用绝对路径。 

相对导入
- from . import module_name。导入和自己同目录下的模块。
- from .package_name import module_name。导入和自己同目录的包的模块。
- from .. import module_name。导入上级目录的模块。
- from ..package_name import module_name。导入位于上级目录下的包的模块。


当从一个包含类的模块中导入类时，常常这么写：

    from myclass import MyClass
    from foo.bar.yourclass import YourClass

如果上述的写法导致名字的冲突，那么这么写：

    import myclass
    import foo.bar.yourclass

然后使用`myclass.MyClass`和`foo.bar.yourclass.YourClass`。

避免通配符的导入（from import *），因为这样做会不知道命名空间中存在哪些名字，会使得读取接口和许多自动化工具之间产生混淆。

## 字符串引号
在Python中，单引号和双引号字符串是相同的。PEP不会为这个给出建议。选择一条规则并坚持使用下去。当一个字符串中包含单引号或者双引号字符的时候，使用和最外层不同的符号来避免使用反斜杠，从而提高可读性。 

## 空格

### 不能忍受的事情

在下列情况下，避免使用无关的空格：
紧跟在小括号，中括号或者大括号后。

    Yes: spam(ham[1], {eggs: 2})
    No:  spam( ham[ 1 ], { eggs: 2 } )

紧贴在逗号、分号或者冒号之前。

    Yes: if x == 4: print x, y; x, y = y, x
    No: if x == 4 : print x , y ; x , y = y , x

然而，冒号在切片中就像二元运算符，在两边应该有相同数量的空格（把它当做优先级最低的操作符）。在扩展的切片操作中，所有的冒号必须有相同的间距。例外情况：当一个切片参数被省略时，空格就被省略了。

    # 推荐：
    ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
    ham[lower:upper], ham[lower:upper:], ham[lower::step]
    ham[lower+offset : upper+offset]
    ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
    ham[lower + offset : upper + offset]

    # 不推荐：
    ham[lower + offset:upper + offset]
    ham[1: 9], ham[1 :9], ham[1:9 :3]
    ham[lower : : upper]
    ham[ : upper]

紧贴在函数参数的左括号之前。

    Yes: spam(1)
    No: spam (1)

紧贴索引或者切片的左括号之前。

    Yes: dct['key'] = lst[index]
    No: dct ['key'] = lst [index]

为了和另一个赋值语句对齐，在赋值运算符附件加多个空格。 

    # 推荐：
    x = 1
    y = 2
    long_variable = 3

    # 不推荐：
    x             = 1
    y             = 2
    long_variable = 3
 

### 其他建议

避免在尾部添加空格。因为尾部的空格通常都看不见，会产生混乱：比如，一个反斜杠后面跟一个空格的换行符，不算续行标记。有些编辑器不会保留尾空格，并且很多项目（像CPython）在pre-commit的挂钩调用中会过滤掉尾空格。
总是在二元运算符两边加一个空格：赋值（=），增量赋值（+=，-=），比较（==,<,>,!=,<>,<=,>=,in,not,in,is,is not），布尔（and, or, not）。
如果使用具有不同优先级的运算符，请考虑在具有最低优先级的运算符周围添加空格。有时需要通过自己来判断；但是，不要使用一个以上的空格，并且在二元运算符的两边使用相同数量的空格。

    # 推荐：
    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)

    # 不推荐：
    i=i+1
    submitted +=1
    x = x * 2 - 1
    hypot2 = x * x + y * y
    c = (a + b) * (a - b)

在制定关键字参数或者默认参数值的时候，不要在=附近加上空格。 

    # 推荐：
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)

    # 不推荐：
    def complex(real, imag = 0.0):
        return magic(r = real, i = imag)

功能型注释应该使用冒号的一般性规则，并且在使用->的时候要在两边加空格。（参考下面的功能注释得到能够多信息）

    # 推荐：
    def munge(input: AnyStr): ...
    def munge() -> AnyStr: ...

    # 不推荐：
    def munge(input:AnyStr): ...
    def munge()->PosInt: ...

当给有类型备注的参数赋值的时候，在=两边添加空格（仅针对那种有类型备注和默认值的参数）。 

    # 推荐：
    def munge(sep: AnyStr = None): ...
    def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

    # 不推荐：
    def munge(input: AnyStr=None): ...
    def munge(input: AnyStr, limit = 1000): ...

复合语句(同一行中的多个语句)通常是不允许的。 

    # 推荐：
    if foo == 'blah':
        do_blah_thing()
    do_one()
    do_two()
    do_three()

    # 最好别这样：
    if foo == 'blah': do_blah_thing()
    do_one(); do_two(); do_three()

虽然有时候将小的代码块和 if/for/while 放在同一行没什么问题，多行语句块的情况不要这样用，同样也要避免代码行太长！ 

    # 最好别这样：
    if foo == 'blah': do_blah_thing()
    for x in lst: total += x
    while t < 10: t = delay()

    # 绝对别这样：
    if foo == 'blah': do_blah_thing()
    else: do_non_blah_thing()

    try: something()
    finally: cleanup()

    do_one(); do_two(); do_three(long, argument,
                                list, like, this)

    if foo == 'blah': one(); two(); three()


## 注释

与代码相矛盾的注释比没有注释还糟，当代码更改时，优先更新对应的注释！

注释应该是完整的句子。如果一个注释是一个短语或句子，它的第一个单词应该大写，除非它是以小写字母开头的标识符(永远不要改变标识符的大小写！)。

如果注释很短，结尾的句号可以省略。块注释一般由完整句子的一个或多个段落组成，并且每句话结束有个句号。

在句尾结束的时候应该使用两个空格。

当用英文书写时，遵循Strunk and White （《Strunk and White, The Elements of Style》）的书写风格。

在非英语国家的Python程序员，请使用英文写注释，除非你120%的确信你的代码不会被使用其他语言的人阅读。

### 块注释
块注释通常适用于跟随它们的某些（或全部）代码，并缩进到与代码相同的级别。块注释的每一行开头使用一个#和一个空格（除非块注释内部缩进文本）。

块注释内部的段落通过只有一个#的空行分隔。

### 行内注释
1.有节制地使用行内注释。

2.行内注释是与代码语句同行的注释。行内注释和代码至少要有两个空格分隔。注释由#和一个空格开始。

事实上，如果状态明显的话，行内注释是不必要的，反而会分散注意力。比如说下面这样就不需要：

    x = x + 1                # Increment x

但有时，这样做很有用：


    x = x + 1                # Compensate for border

### 文档字符串
要为所有的公共模块，函数，类以及方法编写文档说明。

非公共的方法没有必要，但是应该有一个描述方法具体作用的注释。这个注释应该在`def`那一行之后。

PEP 257描述了写出好的文档说明相关的约定。特别需要注意的是，多行文档说明使用的结尾三引号应该自成一行，例如：


    """Return a foobang

    Optional plotz says to frobnicate the bizbaz first.
    """

对于单行的文档说明，尾部的三引号应该和文档在同一行。

    """Return an ex-parrot."""

