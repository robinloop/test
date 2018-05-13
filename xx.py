# -*- coding: UTF-8 -*-

print('中国hello')


def func():
    pass


def out(a):
    print(a, type(a))


out('xxx123')
out(123445)

a = [i for i in range(10) if i % 2 == 0]
print(a)

D = {x.upper(): x * 3 for x in 'abcd'}
print(D)

a = 'a' * 3
print(a)
L = [x * 3 for x in 'sdb']
print(L)
