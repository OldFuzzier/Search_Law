#!/usr/bin/python
# -*- coding: utf-8 -*-
from search_engine import search


# 测试查询引擎
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