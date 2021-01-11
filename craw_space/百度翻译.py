# -*- coding:utf-8 -*-
#!usr/bin/env python
import requests
import json

if __name__ == '__main__':
    url = ' https://fanyi.baidu.com/sug'
    kw = input('please input a word')
    data = {
        'kw': kw
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    response = requests.post(url, data=data, headers=headers)
    res_obj = response.json()
    # 持久化储存
    fileName = kw + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(res_obj, fp=fp, ensure_ascii=False)
    print(res_obj)
    # fileName = kw + '.html'
    # with open(fileName, 'w', encoding='utf-8') as fp:
    #     fp.write(page_text)
    # print(fileName, '保存成功', 'over ')