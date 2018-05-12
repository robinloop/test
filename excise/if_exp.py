# -*- coding: UTF-8 -*-

import math


def get_log(x):
    if x > 0:
        return math.log(x)
    else:
        return float('nan')


x = 5
log_val1 = get_log(x)
log_val2 = math.log(x) if x > 0 else float('nan')
print(log_val1, log_val2)

print('找出1000内的偶数：')
L = [x for x in range(1000) if x % 2 == 0]
print(L)
print(type(L))

# 列表合并
print('列表合并(+)：', [1, 2] + [3, 4])

# 列表重复
print('列表重复(*)：', [1, 2] * 5)

# 判断元素是否在列表中
print('判断元素存在(in)：', 1 in L, 2 in L)

t = (1, 'a', 2, 'b')
# 解包 unpack
a, b, _, _ = t
print('unpack: ', t)

# 确保unpack接收的变量个数和tuple的长度相同，否则报错
# 经常出现在函数返回值的赋值时
# a, b, c = t


d = {'小象学院': 'http://www.chinahadoop.cn/',
     '百度': 'https://www.baidu.com/',
     '阿里巴巴': 'https://www.alibaba.com/',
     '腾讯': 'https://www.tencent.com/'}

print('通过key获取value: ', d['小象学院'])

# 遍历key
print('遍历key: ')
for key in d.keys():
    print(key)

# 遍历value
print('遍历value: ')
for value in d.values():
    print(value)

# 遍历item
print('遍历item: ')
for key, value in d.items():
    print(key + ': ' + value)

# format输出格式
print('format输出格式：')
for key, value in d.items():
    print('{}的网址是{}'.format(key, value))

bd = d.pop('百度')
print(bd)


print('创建set:')
my_set = {1, 2, 3}
print(my_set)
my_set = set([1, 2, 3, 2])
print(my_set)

print('添加单个元素:')
my_set.add(3)
print('添加3', my_set)

my_set.add(4)
print('添加4', my_set)

print('添加多个元素：')
my_set.update([4, 5, 6])
print(my_set)