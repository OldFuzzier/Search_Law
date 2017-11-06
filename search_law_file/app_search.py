#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, abort, render_template
from search_engine import MySearch
from utils import add_order

app = Flask(__name__)


@app.route('/', methods=['GET'])
def v_index():
    return render_template('index.html', name='刑法查询')


@app.route('/search', methods=['GET'])
def v_search():
    try:
        query = request.args['query']
        law_list = MySearch().search_word(query)  # tup是number和content组成的
        return render_template('search.html', o_law_list=law_list, name='刑法条款')
    except Exception, e:
        print e
        return render_template('error.html', info='你查询的关键词没有在刑法内容内')


@app.route('/api', methods=['GET'])
def json_api():
    '''
    该方法提供了法律查询的接口，返回json化后的结果
    返回数据的结构为：
    {task:  {the order: [law_number, sketch of laws, complete laws],
        	the order: [law_number, sketch of laws, complete laws]},
            ...
    }
    '''
    try:
        word = request.args['info']
        law_lst = MySearch().search_word(word)  # tup是number和content组成的
        o_law_list = add_order(law_lst)  # 给tuple加入序号, 并转换为api的数据结构
        return jsonify({'task': o_law_list}), 200
    except Exception, e:
        print e
        abort(400)
        return


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
