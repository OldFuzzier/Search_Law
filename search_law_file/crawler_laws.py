#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


url_criminal = 'http://www.lawtime.cn/faguizt/23.html'
url_civil = ''


def get_html(url):
    headers = {'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/30.0.1581.2 Safari/537.36'}
    text = requests.get(url, headers=headers).text
    return text


def parser_html(html):
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


def main():
    html = get_html(url_criminal)
    laws_lst = parser_html(html)
    return laws_lst

'''
Test:

string =<div><p>im a title</p>
            dafafaf
            hahhahhahhha</div>
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <div>hehe</div>
            <p>4</p>

soup = BeautifulSoup(string, 'lxml')
print soup.find('div').attrs == {}

for i in soup.find('div').next_siblings:
    if i != '\n':
        if i.name != 'p':
            break
        print i
end
'''


