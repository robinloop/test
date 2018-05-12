# -*- coding: UTF-8 -*-
import  numpy as np

mylist = [i for i in range(1,10)]
print(mylist)
x = np.array(mylist)
print(x)
L = np.arange(1, 10, 1, dtype=int)
print(L, len(L))
Lr = L.reshape((3,-1))
print(Lr)
print(Lr[Lr > 3])
print(Lr.T)
print(Lr.transpose())
print(Lr.mean(), Lr.sum(), Lr.max(), Lr.min(), Lr.std())
print(Lr.all())
print(Lr.any())

# 一维array
s = np.arange(13) ** 2
print('s: ', s)
print('s[0]: ', s[0])
print('s[4]: ', s[4])
print('s[0:3]: ', s[0:3])
print('s[[0, 2, 4]]: ', s[[0, 2, 4]])

for row in Lr:
    print('row =', row)

for i, row in enumerate(Lr):
    print('row {} is {}'.format(i ,row))

t2 = Lr ** 2
print(t2)

for i, j in zip(Lr, t2):
    print('{} + {} = {}'.format(i, j, i+j))

print(zip(Lr, t2))