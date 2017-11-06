#!/usr/bin/python
# -*- coding: utf-8 -*-
from search_engine import MySearch
from process_database import ProcessDB


# 测试查询引擎
def test_engine():
    # temp = ['嫌疑人在知道犯错情况下再次犯错', '如果强奸未成年少女判死刑,嫌疑人和共犯一样', '杀人犯也是迫不得已']
    inp = ''
    while inp != 'exit':
        inp = raw_input('Please input:\n')
        lst = MySearch().search_word(inp)
        for i in lst:
            print i
            print
        print 'total lines: ' + str(len(lst))
    return

def test_db():
    pdb = ProcessDB()
    data_list = pdb.get_number_content_all()
    return data_list[:2]

if __name__ == '__main__':
    test_engine()
