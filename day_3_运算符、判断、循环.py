# path = r'C:\Users\newbee\Desktop'
# print(path)


# input类型默认为str, str 相加 = 字符串拼接 'A' + 'B' = 'AB'
# fetch_user = input().split()# str.split(分割符, 最大数量)

# 不能把eval写作系统与用户输入的操作相关，因为eval会自动执行它： 平时用来，字段转化类型，比如说
# 字符串列表转列表类型--> [1, 2, 3, 4, 5]
# print(type(eval(input('input:'))))

# num1 = 30
# num2 = 30
#
# # +
# result_1 = num1 + num2  # 20+30
# print(f'result_1: {result_1}')
# # -
# result_2 = num1 - num2  # 20+30
# print(f'result_2: {result_2}')
# # *
# result_3 = num1 * num2  # 20+30
# print(f'result_3: {result_3}')
# # /
# result_4 = num1 / num2  # 20+30
# print(f'result_4: {result_4}')
#
# # % --> 除数除第一次，剩下的余数就是它的结果，这个常用在于分块
# # for i in range(1, 11):
# #     if (i % 2 ==0):
# #         print(i)
# result_5 = num1 % 2
# print(f'result_5: {result_5}')
#
# # **
# # *是乘法，**是次幂 左操作数 ** 幂数 = 左操作数的n次幂
# result_6 = 2 ** 3
# print(f'result_6: {result_6}')
#
# # //
# result_7 = 7 // 3  # 2 |.33333333| 直接取整数部分，不看小数部分
# print(result_7)

# 位运算符
"""
a = 0011 1100
b = 0000 1101
    高位  低位
"""
# << 左移操作符：每次左挪1位，在数学层面本质是 x 2
# a << 2
# 1111 0000 # 低位补0，高位丢弃
# a << 2
# 1100 0000 # 低位补0，高位丢弃

# >> 右移操作符：每次右挪1位，在数学层面本质 ÷ 2
# 1100 0000 # 高位补0，低位丢弃
# a >> 2
# 0011 0000 #
# a >> 2
# 0000 1111

# & 按位 与 运算符
"""
a = 0011 1100
b = 0000 1101
    高位  低位
a & b = 0000 1100
"""

# | 按位 或 运算符
"""
a = 0011 1100
b = 0000 1101
    高位  低位
a | b = 0011 1101
"""

# ^ 按位异或运算符：当两对应的二进位 相异 时，结果为1
"""
a = 0011 1100
b = 0000 1101
    高位  低位
a ^ b = 0011 0001
"""

# ~ 按位取反运算符
# (~a)
# ^ 按位异或运算符：当两对应的二进位 相异 时，结果为1
"""
a = 0011 1100
    高位  低位
~a = 1100 0011
"""

# 比较运算符
# =<
# =>
# 10 < a < 20 # C不行  a > 10 && a < 20

# 布尔(逻辑)运算符
# and
# a > 10 && a < 20  a > 10 and a < 20
# or
# a == 10 或者 a == 20
# a == 10 or a == 20
# not
# not (a > 10 and a < 20) --> True --> False
# True --> False
# False --> True


# 赋值运算符
# a = 20
# b = 30
# c = a + b  # =
# c += a  # c = c + a
# c -= a  # c = c - a
#
# # 优先级：算术优先级 > 位运算符 > 比较运算符 > 布尔运算符 > 赋值运算符 可以用括号去调整优先级
# # 最内层的括号最先算
# # 十进制 --> 二进制 二进制下众生平等 x 2
# c = (a + (b >> 2 > 3) and (a - b << 2))

# 生成数，平时我们会在某些场景内，需要生成一段区间的数字，比如说，我们想计算1 ~ 100的相加结果
# 可以先生成 1~100，再一口气相加
# python就可以用range语法生成
# range(最先开始的位置[最小数, 默认为0], 最大位置 - 1, 步长[每一次增加的步数, 默认]
# 1~100 range(1, 100 + 1, 1)
# python默认的range写法是range(最大数-1)，因为其他两个数都是有默认的
# 所以，我们想生成0~n的数就是，range(n + 1)
# 我们想生成n个数就是，range(n) 10, 0~9 = 0,1,2,3,4,5,6,7,8
# 总结一下可以生成 [ 左闭右开区间 ]的范围数字

#
# print(list((range(9))))
#
#
# print('我很厉害') # 输出6遍，怎么做？
# print('我很厉害') # 输出6遍，怎么做？
# print('我很厉害') # 输出6遍，怎么做？
# print('我很厉害') # 输出6遍，怎么做？
# print('我很厉害') # 输出6遍，怎么做？
# print('我很厉害') # 输出6遍，怎么做？
# # 可以直接用输出6次print实现，但是我们可以用循环
# print('====================================')
# # 循环：
# # for
# # 把某个可以循环的变量，给到循环里面去执行
# # 比如，我们可以让程序走n遍就可以用range(n)
# # for [循环变量] in [需要被从中一个个抽取元素的主体]: --> 有一个冒号
# #     # 循环体，缩进一段距离
# #
# print(list(range(6)))
# for x in range(6): # n - 1      0, 1, 2, 3, 4, 5
#     # 把range里面的值，一个个给到x，x表示了range里的每一个元素
#     print(f'我很厉害, 第{x}次')
# # 需要被从中一个个抽取元素的主体: 可以迭代，可迭代对象 --> 不断的往下迭代更换，直到不能迭代为止
# # 可迭代对象: str --> 字符串
# # for 循环变量 in 循环主体:
# # 循环变量：每一次迭代中，表示循环主体里的当前迭代轮次的元素
# # 我们可以在循环中使用循环变量
# char = 'Hello World'
# for ch in char:
#     print(ch) # 循环作用域
# # 作用域外
# print(char)
#
# for i in range(3):
#     print(f'跑了第{i+1}次')
# else:       # 在它正常跑完之后，我们就可以执行else语句
#     print('跑完了')
#     # 不正常跑完：break, continue, 程序异常报错-->程序终止
# break # 强行终止循环
# for i in range(100000000):
#     # 正常情况下，循环会跑100000000次会停止
#     # 现在，我们想让他在第10次就终止了
#     print(f'跑了第{i+1}次')
#     if (i + 1 == 10): # 第10次的时候，就退出
#         break # 终止循环,直接结束掉,不管后面的了
# print(i)
# 遇到空格就结束
# for i in 'Hello World':
#     if (i == ' '): # 判断字符是不是空格
#         break
#     print(i)    # 输出字符

# continue # 跳过本轮循环
# for i in 'Hello World':
#     if (i == ' '): # 判断字符是不是空格
#         continue
#     print(i)
"""
调试：
c = 1 + 2
step_1: 1： 把1挪到一个盒子a里
step_2: 2： 让他盒子a里的数相加，并存在盒子B
step_3: c:  把盒子B的值给到C
step_4: 结束计算

步过：操作的细节底层不看，直接跳过看结果  直接看C的值，直接到step3
步入：进入操作底层观察执行过程，执行整个过程完才能看到结果 # 从step_1开始看，看到step3
步出：进入底层后，直接跳出当前操作操作看结果 # 进入step_2后，不想看了，可以直接退出到step_4
"""

# def printf(value):
#     print(value)

# for i in range(1, 101): # 1~100
#     if (i % 2 != 0):
#         continue
#     printf(i) # i % 2 == 0 输出，也就是偶数

# for i in range(5):
#     print(i)
#     break  # break就不会执行else
# else:
#     print('执行完了')
# 嵌套循环
# for i in range(10):
#     for j in range(5):
#         print(f'{i}, {j}')
#         if (j == 2):
#             break  # break是j的循环
#         else:
#             continue # continue的是j循环
#     if (i == 5):
#         break  # i 结束
# 循环里面嵌套着循环
# 在使用braek或continue的时候，会处理掉它这个作用域里面的循环，
# 最内层的处理最内层，外层break/continue会影响内层循环

# while
# while (条件为真):
# i = 0
# while i < 10: # 条件成立
#     print(i)
#     i += 1

# 算法--> 左右两边向中间聚拢，还有二分
# i = 0
# 100 / 2
# 50 / 2
#
# left = 0
# right = 100
# while (left < right):
#     left += 1
#     right -= 1
# while i < 10:
#     print(i)
#     i += 1
# else: # while也能使用else
#     print('执行完了')
# 无限循环, 永不停止
# 条件为真 = True = 1
# 条件为否 = False = 0
# count = 1
# while True:
#     print(f'第{count}次循环')
#     count += 1
#     # 无限循环是不会停下来的，必要时，我们可能需要结束
#     if (count == 50):
#         break # break直接结束循环
# condition = 1
# count = 1
#
# while condition:
#     print(f'第{count}次循环')
#     count += 1
#     # 无限循环是不会停下来的，必要时，我们可能需要结束
#     if (count == 50):
#         condition = 0 # break直接结束循环

# while (not False): # == True
#     print('循环中...')

# 到底什么情况为真
# 与其说什么时候为真，直接说什么时候为假更好
# 必定为假情况: 值为0，False 的本质也是0. 空字符串，空的数据都为0，还有None
# 其余均为真
# a = None
