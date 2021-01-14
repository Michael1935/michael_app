# -*- coding:utf-8 -*-
#!usr/bin/env python
import requests
import json

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    for id in range(1, 6):
        page = str(id)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':''
        }

        json_ids = requests.post(url=url, data=data, headers=headers).json()
    id_list = []
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    # 获取企业详情数据
    #
    print(id_list)
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    all_data_list = []
    for id in id_list:
        data = {
            'id': id
        }
        detail_data = requests.post(url=post_url, data=data, headers=headers).json()
        print(detail_data)
        all_data_list.append(detail_data)
    fp = open('./detail.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)

