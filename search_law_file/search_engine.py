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
        pass

    # 查询句子，用到在线分词api，所以效率降低
    # search方法主要执行逻辑是
    # 1 对输入字符串进行拆分成每一个词
    # 2 提取所有法律条款
    # 3 找出所有在词在的法律
    # 4 去重
    # 5 返回搜索结果
    def search_sentence(self, sentence):
        content_list = ProcessDB().get_content_all()  # 获取全部content
        format_words = filter(lambda x: len(x) > 1, jieba.lcut(sentence))  # 对输入的字符串进行分词、筛选
        total_lst = []
        for word in format_words:
            total_lst.extend(filter(lambda law: law.find(word) != -1, content_list))
        total_set = set(total_lst)  # 去重
        return total_set

    # 查询单个词
    def search_word(self, word):
        number_content_list = ProcessDB().get_number_content_all()  # 获取全部number和content
        total_lst = filter(lambda tup: tup[1].find(word) != -1, number_content_list)
        return total_lst

