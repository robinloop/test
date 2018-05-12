# -*- coding: UTF-8 -*-

import csv
import operator

data_file = './data/BeijingPM20100101_20151231.csv'
with open(data_file, 'r') as csvfile:
    a = csv.DictReader(csvfile)
    # for row in a:s
    # print(row)
    data = list(a)
    print(len(data))
    print(data[0].keys())
    sum_ds = sum(float(row['PM_Dongsi']) for row in data if row['PM_Dongsi'] != 'NA')
    print('PM_Dongsi sum = ', sum_ds)

    aaa = set(row['month'] for row in data)
    print(aaa)
    ml = list(aaa)
    import functools

    key = functools.cmp_to_key(lambda x, y: int(x) - int(y))
    print(sorted(ml, key=key))

    # b = map(lambda x, y: cmp(x, y), ml)
    print()

# print(list(a))list(a)

# for x in list(a):
#     print(x)

# a = np.zeros((5, 5))
# print(a)
# print(a.ndim)
# a[0, 0] = 33
# a[1, 1] = 22
# a[2, 3] = 11
# d = [1, 2, 2]
# print(a)
# print(a[0, 0])
# print(a[:2, 0:5])
# print(a > 4)
# print(a[a > 4])
# a[a < 5] = 2
# print(a)
# a = np.full((3, 5), 4)
# print(a)
# print(a.T)
# print(a.T.transpose())
# a = np.arange(1,10)
# print('a=', a, a.shape)
# b = a.reshape(-1, 1)
# print('b = ', b, b.shape)
