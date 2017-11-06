#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

from crawler_laws import MyCrawler


# mysql配置类
class SettingDB(object):

    def __init__(self):
        self._config = dict(host='127.0.0.1', user='root', passwd='wt322426', db='law_database')

    # 为处理mysql的方法提供配置和异常处理的装饰器
    def __call__(self, func):
        def process_inner(other_obj, *args, **kwargs):
            try:
                other_obj._conn = MySQLdb.connect(**self._config)
                other_obj._cur = other_obj._conn.cursor()
                '''resolve UnicodeEncodeError: 'latin-1' codec can't encode character'''
                other_obj._conn.set_character_set('utf8')
                other_obj._cur.execute('SET NAMES utf8;')
                other_obj._cur.execute('SET CHARACTER SET utf8;')
                other_obj._cur.execute('SET character_set_connection=utf8;')
                '''end'''
                return func(other_obj, *args, **kwargs)
            except Exception, e:
                print 'Error: ' + e
                other_obj._conn.rollback()
            finally:
                other_obj._cur.close()
                other_obj._conn.close()

        return process_inner


# mysql处理类
class ProcessDB(object):

    def __init__(self):
        pass

    # 从相关法律查询网站提取信息存入db
    @SettingDB()
    def save_in_db(self):
        lst = MyCrawler().run()  # 获取法律列表
        for law in lst:
            num = law[0]
            cont = ';'.join(law[1:])
            sql = 'insert into criminal (number,content) values (%s,%s)'
            params = (num, cont)
            self._cur.execute(sql, params)
        self._conn.commit()
        return

    # 查询所有content
    @SettingDB()
    def get_content_all(self):
        sql = 'select content from criminal'
        self._cur.execute(sql)
        tuple_lst = self._cur.fetchall()
        data_lst = map(lambda x: x[0], tuple_lst)  # format tuple
        return data_lst

    @SettingDB()
    def get_number_content_all(self):
        sql = 'select number, content from criminal'
        self._cur.execute(sql)
        data_list = self._cur.fetchall()
        return data_list

    # 查询指定content的number
    @SettingDB()
    def get_number_by_content(self, content):
        sql = 'select number from criminal where content=%s'
        self._cur.execute(sql, params=(content,))
        data = self._cur.fetchone()[0]
        return data

    # 查询指定id的所有列
    @SettingDB()
    def get_info_by_id(self, _id):
        sql = 'select * from criminal where id = %s'
        self._cur.execute(sql, params=(_id,))
        data = self._cur.fetchone()[0]
        return data

