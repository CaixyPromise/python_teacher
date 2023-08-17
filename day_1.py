# 英文字母
# ()
# , . ? ! @

"""
两类型语言：1、解释型语言； 2、编译型语言

1、解释型语言
有一个软件叫做解释器，解释器去解释我们的代码，并执行对应操作
解释器通常是一行一行的解释代码，并操作，代码跑到哪里就是哪里。
代表语言：Python\Java

2、编译型语言
有一个软件叫做编译，器我们把所有代码写好之后，用编译器把所有代码编译成计算机能够看懂的语言。
计算机再通过这个他能看懂的语言去执行我们对应的代码。如果编译过程中，代码有问题，程序就停止编译。
编译完成后，程序就可以正常的运行。但是，如果在运行的过程中出现问题，程序就会被系统强制退出。
代表语言：C语言、C++
"""

# 输出语句

# print(1)
# a = 1 / 0
# print('Hello World')

# name = "caixy"
# age  = 22
# sex  = "man"
#
# print(name)
# print(age)
# print(sex)

# 计算机的存储空间：硬盘、内存、寄存器（先不管）
# 硬盘就是持久化存储，所有的文件都是存放在硬盘上
# 内存是处理器与你的硬盘交互过程的中间站，你的所有硬盘内的文件，需要被使用的时候，都会先存入到内存中，才会被CPU读取。

# delete: 删除变量
# del name
# del age
# del sex
# print(name)
# print(age)
# print(sex)


"""
①不得使用作为数字开头；

③不得使用空格，可以用下划线连接变量名称；

④不得使用标识符号（#）在其中；

⑤不得使用中文作为变量名称；

⑥不得使用以下关键字作为开头
"""

# 变量名 = 变量值
# name = 'zrh'
# age = 18
# user_gender = 'man'
# #'123 = '123''
#
# """简记：2种情况不能做开头：数字、
#         3种情况不允许出现：空格、标识符（#）、中文、关键字单独出现"""


# 缩进
# a = 10
# if a == 10: # 冒号在python里面，是代表，一个缩进开始
#     # 缩进 = 4个空格 = 1个TAB键的范围
#     # 缩进进入之后，如果没有非常严重的代码错误，程序就会执行这一段缩进里的所有代码，才会退出自己的缩进空间，返回上一层
#     print('执行if !')
#     print('if a == 10语句执行中！')
#     if a >= 10:
#         print('a >= 10')
#     if a > 20:
#         print('a > 20')
#     print('if a == 10语句即将退出！！')
#     b = 20
#     print('enter')
#     print(b)
# print('Leave')
# print(b)
# print('Process finished with exit code 0.')


# a = 10
# b = 10
# print(a)  # 输出变量
# print(3)  # 直接输出数字
# print('Hello')  # 添加引号可以直接输出文本
# print()  # 直接输入print()会换行
# print(1+2)  #  直接输出算数结果
# print(a == b)
#
# c = '''Hello
# C'''
#
# print('''Hello
# World''')
# print(c)


# age = 10 # 在人类的视角里，10，它是一个数字；在计算机里，它是一个整数型的变量int
# name = 'caixy'  # 平时：文字；在计算机：它是一个 [字符串] 型 str
# pai = 3.14 # 平时：小数；计算机里：浮点数 = 小数 float
# bool_t, bool_f = True, False    # 平时：是 / 否；计算机：布尔值 bool

# int num = 98;
# const char* = "hello world";
# int_ = 98
# float_ = 3.1415
# bool1 = True
# bool2 = False
# str_ = 'Hello everyone!'
# # 输出变量的数据类型
# # print(type(变量名称或值))
#
#
# print(f'int_是{int_}，数据类型是 {type(int_)}\n')  # 通常的，直接写出的整数是int整数类型。
# print(f'float_是{float_}，数据类型是 {type(float_)}\n')  # 通常的，直接写出的小数是fLoat浮点数类型。
# print(f'bool1是{bool1}，数据类型是 {type(bool1)}\n')  # 通常的，直接写出的True是布尔值类型。
# print(f'bool2是{bool2}，数据类型是 {type(bool2)}\n')  # 通常的，直接写出的False是布尔值类型。
# print(f'str_是{str_}，数据类型是 {type(str_)}')  # 通常的，直接写出带引号的文本是字符串类型。


 # 数据类型转换：只需要将想转化的数据类型写出来，并在括号内写入变量名称即可
 # 新类型名称(需要转化的变量或值)
# new_int_float = float(int_) # 整型 转 浮点数，直接在末尾+.0
# new_float_int = int(float_) # 浮点数 转 整数，直接把小数点右边的数值全部丢掉，取整数
# new_bool1_int = int(bool1)  # True  = 1
# new_bool2_int = int(bool2)  # False = 0
# new_int_str = str(int_)     # 整型 转 字符串，直接把它的定义类型转字符串表示就行
# # 字符串转整型呢？有可能会出错，出错的地方只会出现在，字符串的内容里面有不是数字的，就会出错
# print(int('123')) # 可以
# print(int('123a')) # 不可以，因为a不是数字
#
#
# print(f'int_是{int_}，新的int_到float的值是{new_int_float}，数据类型是{type(new_int_float)}\n')
# print(f'float_是{float_}，新的float_到int的值是{new_float_int}，数据类型是{type(new_float_int)}\n')
# print(f'bool1是{bool1}，新的bool1到int的值是{new_bool1_int}，数据类型是{type(new_bool1_int)}\n')
# print(f'bool2是{bool2}，新的bool2到int的值是{new_bool2_int}，数据类型是{type(new_bool2_int)}\n')
# print(f'int_是{int_}，新的int_到str的值是{new_int_str}，数据类型是{type(new_int_str)}\n')


name = 'caixy'
age = 22

# print(name)
# print(age)
# 连接起来输出

# 会报错，字符串只能连接字符串
# print(name + age)
# 我们需要转化age的数据类型一致，因为name不能转成整型类型

# 在python里，两个字符串相加，本质就是把他们拼起来就行~
# a ='A'
# b ='B'
# print(a+b)

# 我叫 xxx，今年 xxx岁了
# 正常拼接方式
# print('我叫' + name + ', 今年' + str(age) + '岁了')

# %号拼接
# 我叫 xxx，今年 xxx岁了
# template = '我叫 %s，今年 %d 岁了'%(name, age)

# format拼接
# 直接使用
# template = '我叫 {}，今年 {} 岁了'.format(name, age)

# 标定位置
# 计算机表示位置的方法，总是从0开始计数。现实中表示1-10，计算机会表示成 0-9
# template = '我叫 {1}，今年 {0} 岁了'.format(name, age)

# 特定位置填特定名称呢？
# template = '我叫 {_name}，今年 {_age} 岁了'.format(_age = age, _name = name)
# print(template)

# f-string
# template = f'我叫 {name}，今年 {age} 岁了, type_name is: {type(name)}'
# print(template)


# 格式化字符串：小数点精度
# %
pai = 3.1415926
# tempalte = 'pai: %.3f'%(pai) # %.nf 精确n位小数
# print(tempalte)

# format
# template = 'pai: {0:.5f}'.format(pai) # {:.nf} 精确到n位小数
# print(template)

# f-string
# template = f'pai: {pai:.5f}' # 变量名:.nf 精确到n位小数
# print(template)

# 跟着上面的代码过一遍，复习~
# 跟着敲
# 有时间，你把上面的内容按照自己的想法重新复现一遍