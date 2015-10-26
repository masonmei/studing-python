# # coding=utf-8
from decimal import Decimal
#
# __author__ = 'mason'
#
#
# # Programs are composed of modules
# # Modules contain statements
# # Statement contain expressions
# # Expressions create and process objects
#
#
# # Build-in Objects
# # Numbers           123, 123.0, 3+4j, Decimal()
# # Strings           'string', "string", "a 'dog'",
# # Lists             [1, 2, 3]
# # Sets              {'a', 'b', 'c'}
# # Dictionaries      {'name': 'mason', 'age': 28}
# # tuples            (28, 'mason')
# # Files             open('eggs.txt'), open(r'/home/work/test', 'wb')
#
# # 定义一个整型变量, 没有范围限制
# a = 1234
# b = -23
# c = 9999999999999999999999999999999
# d = c * c
# print d
#
# # 定义一个8进制数, 以0开头
# octal = 01777777777
# print octal
# octal2 = -01777777777
# print octal2
#
# # 定义一个16进制数, 以0x 或0X 开头
# hex1 = 0xffff
# print hex1
# hex2 = 0Xffff
# print hex2
# hex3 = -0xffffff
# print hex3
#
# # 定义一个2进制数, 以0b 或OB开头
# binary1 = 0b11101
# binary2 = 0B000001
# print binary1, binary2
#
# binary3 = -0b11101
# print binary3
#
# # 定义一个浮点数, 同样没有范围限制
# f1 = 3.1416926
# f2 = 999999999999999999.02
# f3 = f2 * f2
# print f3
# f4 = 0 - f3
# print f4
#
# # 定义一个复杂数字
# complex1 = 3 + 4j
# complex2 = 3.1 + 4j
# complex3 = complex1 + complex2
# print complex3
#
# complex4 = complex1 + 19
# print complex4
#
# complex1 = 4 + 5J + 6j
# print complex1
#
# # 定义一个数组
# li1 = [1, 2, 3, 4, 5]
# print li1
# # 遍历数组
# for i in li1:
#     print i
#
# # 取数组元素
# element = li1[0]
# print element
# # 取数组子数组，取从开始到给定下标。不包含结束下标元素
# subList = li1[:3]
# print subList
# # 取数组子数组，取从某个下标开始到结束
# subList = li1[3:]
# print subList
# # 取数组子数组，取从某个下标开始到给定下标结束
# subList = li1[1:3]
# print subList
#
# # 定义一个集合, 集合中没有重复元素
# set1 = {1, 1, 3, 4, 5}
# print set1
# set1 = set('1111')
# print set1
# set1 = set("abc")
# print set1
# # 遍历集合
# for i in set1:
#     print i
#
# set1 = set("abcfgh")
# set2 = set("defg")
#
# # 取交集
# set3 = set1 & set2
# print set3
#
# # 取并集
# set3 = set1 | set2
# print set3
#
# # 取差集
# set3 = set1 - set2
# print set3
#
# set3 = set1 ^ set2
# print set3
#
# # 添加元素
# set1.add(4)
# print set1
#
# # 删除元素
# set1.remove(4)
# print set1
#
# # 定义字符元素类型的集合
# set1 = {'sd', 'fds'}
# set2 = {'sd', 'fds', 'fds'}
# print set1, set2
#
# # 定义浮点类型的集合
# set1 = {2.1, 4.3}
# print set1
#
# # 定义bool类型变量
# bool1 = True
# bool2 = False
#
# # 定义Decimal类型变量，需要导入decimal.Decimal
dec = Decimal("-1.0")
print dec.copy_abs()
print dec.to_integral_value()
#
# # fra = Fraction(1, 3)
# # fra.
