#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, abort
import random
# import re
import search_engine

app = Flask(__name__)


@app.route('/search/api', methods=['GET'])
def json_api():
    #  pattern = re.compile(r'【.+】')  也可以匹配法律的标题
    words = request.args['info']
    law_lst = search_engine.search(words)
    content = map(lambda x: {str(random.randint(1, 100)): [unicode(x[:50]+'....', errors='ignore'),
                                                           unicode(x, errors='ignore')]}, law_lst)  # 将str转换为unicode，这样不会出现编码问题
    '''Test
    for i in content:
        print i.keys()[0]'''
    return jsonify({'task': content}), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

