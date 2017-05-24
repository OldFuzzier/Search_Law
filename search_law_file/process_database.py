#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import wraps

import MySQLdb

import crawler_laws

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='wt322426', db='law_database')

cur = conn.cursor()

'''resolve UnicodeEncodeError: 'latin-1' codec can't encode character'''
conn.set_character_set('utf8')
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')
'''end'''


def try_except(func):
    @wraps(func)
    def inner(*args):
        try:
            return func(*args)
        except Exception, e:
            print 'Error: ' + e
            conn.rollback()
        finally:
            cur.close()
            conn.close()
    return inner


@try_except
def save_in_db():
    # 获取法律列表
    lst = crawler_laws.main()
    for law in lst:
        num = law[0]
        cont = ';'.join(law[1:])
        sql = 'insert into criminal (number,content) values (%s,%s)'
        params = (num, cont)
        cur.execute(sql, params)
    conn.commit()
    return


@try_except
def get_content_db():
    sql = 'select content from criminal'
    cur.execute(sql)
    tuple_lst = cur.fetchall()
    # format tuple
    data_lst = map(lambda x: x[0], tuple_lst)
    return data_lst


'''
获取db中的number
@try_except
def get_number_db(content):
    sql = 'select number from criminal where content=%s'
    params = content
    cur.execute(sql, params)
    data = cur.fetchone()
    return data

@try_except
def get_info(id):
    sql = 'select * from criminal where id = %s'
    params = id
    cur.execute(sql, params)
    data = cur.fetchone()
    return data
'''


