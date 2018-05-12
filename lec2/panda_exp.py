# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

# 三个都是10，个数少会进行广播操作，所以每一个都是10，有3个
s = pd.Series(10, index=[1, 2, 3])
print(s)

s = pd.Series(10)
print(s)

country1 = pd.Series({'Name': '中国',
                      'Language': 'Chinese',
                      'Area': '9.597M km2',
                      'Happiness Rank': 79})

country2 = pd.Series({'Name': '美国',
                      'Language': 'English (US)',
                      'Area': '9.834M km2',
                      'Happiness Rank': 14})

country3 = pd.Series({'Name': '澳大利亚',
                      'Language': 'English (AU)',
                      'Area': '7.692M km2',
                      'Happiness Rank': 9})

df = pd.DataFrame([country1, country2, country3], index=['CH', 'US', 'AU'])
print(df)

# Series
print(df['Area'])
# DataFrame
print(df[['Area']])

print(df.drop(['Area'], axis=1))
print(df.drop(['CH']))

# array
L = [x for x in range(10)]
print(L)
LD = pd.DataFrame(L)
print(LD)
df.reset_index(inplace=True)
df.rename(columns={'index': '简称'}, inplace=True)
print(df.index, df.columns)
print(df)

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
print(data.duplicated())
print(data.drop_duplicates())
data['v1'] = range(7)
print(data)
print(data.drop_duplicates(['k1']))

# 年龄数据
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

# 分箱的边界
bins = [x for x in range(0, 101, 10)]
print(bins)
cats = pd.cut(ages, bins, right=True, include_lowest=False)
print(cats, cats.codes)
print(cats.categories)
print(pd.value_counts(cats))
# group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
# cats = pd.cut(ages, bins, labels=group_names)
# print(cats.get_values())

print(data)
data['test'] = [5, 6, None, None, None, None, None]
print(data)
# print(pd.get_dummies(data['v1']))
# print(df)
# print(df.pivot_table(values='Happiness Rank', columns='Name', aggfunc=[np.mean, np.min], index='简称', margins_name='All'))


dt = {0: [9, 8, 7, 6], 1: [3, 2, 1, 0]}
a = pd.DataFrame(dt)
print(a)
print(a.loc[0])
print(a.iloc[0])
print(a[1])
print(a[[1]])

print(df)
# df.plot(title='test')
# plt.tight_layout()
# plt.savefig('./test.png')
# plt.show()

print('test start')
arr = np.arange(1, 13).reshape(4, 3)
df = pd.DataFrame(arr)
df[0][0] = np.nan
# df.ix[2] = [3,3,3,3

print(df)
print(df.describe())

# df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, 5]],
#                   columns=list('ABCD'))
print(df.dropna(thresh=3))
