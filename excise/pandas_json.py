# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

# jsonfile = './example.json'
# jsondf = pd.read_json(jsonfile)
# print(jsondf)
# print(jsondf.loc[0])
# print(jsondf[:2])
# print(jsondf.groupby('a'))

excelFile = './11.xlsx'
cols = ['班级', '生物', '政治', '历史', '地理']
excel = pd.read_excel(excelFile, '学生成绩', usecols=[0, 1, 7, 11, 15], index_col=None)
print(excel.columns)

print('**********************************')
ef = excel[cols].copy()
print(ef.describe())
# print(ef[cols[1:]].sum(axis=1))
for course in cols[1:]:
    # pandas的std方法计算 的是样本标准差（n-1）
    # 使用以下方法转换为总体标准差
    std = ef[course].std() * np.sqrt((ef[course].count() - 1) / ef[course].count())
    ef[course + '标准分'] = 50 + 10 * (ef[course] - ef[course].mean()) / std

    # ef[course + '分位数'] = ef[course].quantile()
#  使用向量计算总分，各科目分数相加
# ef['total'] = ef[cols[1]] + ef[cols[2]] + ef[cols[3]] + ef[cols[4]]
# 使用切片划分新的dataframe计算总分
ef['总分'] = ef[cols[1:]].sum(axis=1)
# print(ef.sort_values(by=['total'], ))
ef['总分排名'] = ef['总分'].rank(ascending=False, method='min')
ef.index.name = 'index'
# print(ef.head(10))
ef.to_excel('./test.xlsx', index=False, )
print(ef.head(10))

# 获取11班数据
# nef = ef.set_index(['班级'])
# print(nef.ix['11班'].describe())


grouped = ef[cols[1]].groupby([ef[cols[0]]])
print(grouped.describe())
print(ef[cols])
print(ef[cols].groupby(cols[0]).describe()[cols[1]])
