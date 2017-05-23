#!/usr/bin/python
# -*- coding: utf-8 -*-
import jieba

from search_law.search_law_file import process_database as db

'''解决编码问题'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
'''end'''

data_lst = db.get_content_db()  # 获取全部content


def search(words):
    global data_lst
    format_words = filter(lambda x: len(x) > 1, jieba.lcut(words))  # 对输入的字符串进行分词、筛选
    total_lst = []
    for word in format_words:
        total_lst.extend(filter(lambda x: x.find(word) != -1, data_lst))
    total_set = set(total_lst)  # 去重
    return total_set


if __name__ == '__main__':
    temp = ['嫌疑人在知道犯错情况下再次犯错', '如果强奸未成年少女判死刑,嫌疑人和共犯一样', '杀人犯也是迫不得已']
    inp = raw_input('Please input:\n')
    while inp != 'exit':
        inp = raw_input('Please input:\n')
        lst = search(inp)
        for i in lst:
            print i
            print
        print 'total lines: ' + str(len(lst))
