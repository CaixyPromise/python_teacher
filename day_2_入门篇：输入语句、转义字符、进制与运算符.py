
# string = 'Hello My name is: Caixy!!!'

# 转义字符的意思就是：一个特殊的符号，能够让计算机识别，并做出特定操作：换行，退一格，多4个空格，清空行.......

# 转义字符\n
# 转成下面的形式-> \n
"""
Hello
My name is: Caixy!!!

"""
# string_newline = 'Hello\n My name is: Caixy!!!'
# print(string_newline)
#
# # 解释：\r 的作用就是，把\r前面的内容清空掉 --> return
# print('====================================')
# string_return = 'Hello\r My name is: Caixy!!!'
# print(string_return)


# 表示\t: 填充够4个空格
# print('====================================')
# string_tab = 'Hello\t My name is: Caixy!!!'
# print('                                      ')
# print(string_tab)
# print('Hello\tWorld')

# \b字符串内退去一个字符。
# print('back\bspace')

# 在字符串的引号前面加上+r, 可以让转义字符失效
# folder_dir_normal = 'E:\\Code File\\Python\python_teacher\\src\tab.py'
# folder_dir = r'E:\\Code File\\Python\python_teacher\\src\tab.py'
# print(folder_dir_normal)
# print(folder_dir)

# 转义字符跟C语言的基本一致, 甚至大多数语言都共用
# \\ -> \
# print('\\')
# \' -> '
# print('\'')
# \+符号 = 符号自己

# folder = r'E:\Code File\Python\python_teacher\src\\'
# 新填的文件名
# newfile_name = r'abc.txt'

"""
转义字符的应用场景：
1、格式化输出，比如：输出一个表格，或者按照特定形式输出, 仅用在控制台程序中->
  很少用，因为现实中都是有前端负责写界面的
|------------------------------------|
| column_1 |  column_2 | column_3    |
|------------------------------------|

2、文件路径的时候会用到-> 比如文件路径保存 -> 最常见，需要注意到路径之间有没有转义字符导致路径错误
C:\abc\t.txt -> 会出现转义
C:\\abc\\t.txt -> 不会转义
主要两种

转义字符学习的要求：
1、不用死记硬背，记下他的英文单词就行
2、记住常用就行：\n(换行), \\(\), r(让转义字符失效)
3、记住\+符号 = 符号自己
"""


# 输入语句
# 我们按下键盘，让计算机帮我们表达内容，其实就是输入过程
# 我们也能把一段话直接输入给计算机

# use_input = input('请输入用户名:> ')  # 括号内可以添加文本用来提示输入
# print(use_input)

# input->输入的内容，均为str类型，只获取一行的内容
# a = input('请输入a:> ')
# b = input('请输入b:> ')
# print(f'a: {a}')
# print(f'b: {b}')
# print(f'type(a): {type(a)}')
# print(f'type(b): {type(b)}')
# # 字符串相加，本质就是两个字符串连在一起 a = 1, b = 1 --> 1 + 1 = 11
# print(f'a + b = {a + b}')
# a = int(a)
# b = int(b)
# print(a+b)

# 输入完以后直接去转化我们想要转化的类型
# a = int(input('请输入a:> '))
# b = int(input('请输入b:> '))
# print(f'a + b = {a + b}')

#
# a = int(input('请输入数字: a:> ')) --> 假设反骨仔填 abcd，程序会报错退出
# b = int(input('请输入数字: b:> '))
# print(f'a + b = {a + b}')

# 自动根据用户的内容转化类型-->eval
# a = eval(input('请输入: a:> '))
# b = eval(input('请输入: b:> '))
# print(f'type(a): {type(a)}')
# print(f'type(b): {type(b)}')
# print(f'a + b = {a + b}')

# eval 慎用在input语句：因为它会自动调用，自动推导
# __import__('os').listdir()
# print(eval(input()))


# input() 语句高级使用：.split()
# 需要接受用户输入的3个参数
# 1、3个input()
# 一行之内，split
# user_input = input('请输入3个参数, 用-分开:> ').split('-') # split('分割的标识符') 默认是空格
# print(user_input)
# # 直接分开
# name, sex, age = user_input
# print(name, sex, age)

# split('分割的标识符', 最大分割数) 默认是空格，默认全部分割
# user_input = input('请输入3个参数, 用-分开:> ').split('-', 3)
# print(user_input)

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#