# -*- coding:utf-8 -*-
#!usr/bin/env python
import requests
import json
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname':'',
        'pid':'',
        'keyword': '杭州',
        'pageIndex': '1',
        'pageSize': '10'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    response = requests.post(url, data=data, headers=headers)
    list_data = response.json()
    print(list_data)
    fp = open('./kfc.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('kfc over')