#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class MyCrawler(object):

    def __init__(self):
        self.url_criminal = 'http://www.lawtime.cn/faguizt/23.html'

    def get_html(self):
        headers = {'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/30.0.1581.2 Safari/537.36'}
        text = requests.get(self.url_criminal, headers=headers).text
        return text

    def parser_html(self, html):
        total_lst = []
        soup = BeautifulSoup(html, 'lxml')
        law_lines = soup.find_all('p', class_='f-article-title-tiny')
        for line in law_lines:
            #  number; main_content
            line_lst = [i for i in line.stripped_strings]
            # sub_content
            if line.next_sibling.next_sibling.attrs == {}:
                for gen in line.next_siblings:
                    if gen != '\n':
                        if gen.attrs != {}:
                            break
                        else:
                            line_lst.append(gen.string)
                total_lst.append(line_lst)
            else:
                total_lst.append(line_lst)
        return total_lst

    # 主运行程序
    def run(self):
        text = self.get_html()  # 先获取html
        laws_lst = self.parser_html(text)  # 再提取出法律的列表
        return laws_lst


