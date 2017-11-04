#!/usr/bin/python
# -*- coding: utf-8 -*-
import jieba

from process_database import ProcessDB

'''解决环境编码问题'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
'''end'''


class MySearch(object):

    def __init__(self):
        self.data_lst = ProcessDB().get_content_db()  # 获取全部content

    # search方法主要执行逻辑是
    # 1 对输入字符串进行拆分成每一个词
    # 2 提取所有法律条款
    # 3 找出所有在词在的法律
    # 4 去重
    # 5 返回搜索结果
    def search(self, words):
        format_words = filter(lambda x: len(x) > 1, jieba.lcut(words))  # 对输入的字符串进行分词、筛选
        total_lst = []
        for word in format_words:
            total_lst.extend(filter(lambda x: x.find(word) != -1, self.data_lst))
        total_set = set(total_lst)  # 去重
        return total_set
