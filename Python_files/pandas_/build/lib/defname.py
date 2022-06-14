import pandas as pd
import numpy as np
pd.set_option('display.max_columns',None)
from sklearn.feature_extraction.text import CountVectorizer
import jieba # 导入关键字提取库


# python 包


#pandas导入文件
# 路径   编码   文件格式
def improt_data(route,code,format):
    if format == 'csv':
        data = pd.read_csv(route, encoding=code)
    elif format == 'excel':
        data = pd.read_excel(route, encoding=code)
    return data
# return  文件


# 关键字查找
# data :数据
# zi ：关键字
# column ：dataframe字段名称
# 返回列表  输出总订单数量
def wenzi(data, word, column):
    list_2 = []
    list_3 = []
    lis = []
    for row, data_ in data.iterrows():
        name = data_['接单时间']
        list_3.append(name)
        y = data_[column]
        tr = y.find(word)
        if tr > -1:
            list_2.append(y)
    print('关于' + '“' + word + '”' + '的订单数量是：', len(list_2))
    lis.append(list_2)
    lis.append(list_3)
    return lis

# 关键字清理
# list_name ： 字符串列表
# stopwords ： 删除清理关键字
# 返回列表
def clean(list_name_, stopwords_):
    clean_line = []
    for line in list_name_:
        haha = []
        for word in line:
            if word in stopwords_:
                continue
            haha.append(word)
        haha = ','.join(haha)
        clean_line.append(haha)

    return clean_line

# 关键字分词
# column_list： 关键字结巴分词
# 返回列表
def jiebe(column_list):
    text_list = []
    for line in column_list:
        hou = ",".join(jieba.cut(line))
        strlist = hou.split(',')
        text_list.append(strlist)
    return text_list


# 筛选 综合字段
# data:dataframe
# a:字段名称
# 返回  列表  字典  列表
def drop_(data, a):
    df = data.drop_duplicates(subset=a, inplace=False, keep='last')
    list_ = list(df[a])
    list_sum = []
    list_sum_ = []
    list__ = []
    dict_ = {}
    for i in range(len(list_)):
        b = list_[i]
        sum_ = data[data[a] == b][a].count()
        if sum_ > 1:
            list__.append(b)
            dict_[b] = sum_
        else:
            list_sum.append(b)
    k = [list__, dict_, list_sum]
    return k
