#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, abort
import random
# # import re
from search_engine import MySearch

app = Flask(__name__)


'''
该方法提供了法律查询的接口，返回json化后的结果
返回数据的结构为：
{task: {the random number: [sketch of laws, complete laws],
	{the random number: [sketch of laws, complete laws],
	....
}
'''
@app.route('/search/api', methods=['GET'])
def json_api():
    try:
        # pattern = re.compile(r'【.+】')  也可以匹配法律的标题
        words = request.args['info']
        law_lst = MySearch.search(words)
        content = map(lambda x: {str(random.randint(100, 999)): [unicode(x[:50]+'....', errors='ignore'),
                                                               unicode(x, errors='ignore')]}, law_lst)  # 将str转换为unicode，这样不会出现编码问题
        '''Test
        for i in content:
            print i.keys()[0]'''
        return jsonify({'task': content}), 200
    except Exception, e:
        print e
        abort(400)
        return

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

