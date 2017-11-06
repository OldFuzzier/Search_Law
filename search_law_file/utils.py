# -*- coding: utf-8 -*-

# 使用工具


# 给tuple加入序号, 并转换为api的数据结构
def add_order(tuple_list):
    ''' 数据的结构为
    {
    the order: [law_number, sketch of laws, complete laws]},
        	the order: [law_number, sketch of laws, complete laws],
            ...
    }'''
    temp_dict = {}
    for i, tup in enumerate(tuple_list):
        # 将str转换为unicode，这样不会出现编码问题
        # 先转换为tuple，在被添加到dict中
        temp_dict[i+1] = [unicode(tup[0], errors='ignore'),\
                               unicode(tup[1][:100], errors='ignore'),\
                               unicode(tup[1], errors='ignore')]
    return temp_dict


