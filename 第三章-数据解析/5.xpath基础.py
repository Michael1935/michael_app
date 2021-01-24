# -*- coding:utf-8 -*-
#!usr/bin/env python
from lxml import html

if __name__ == '__main__':
    # 将本地的html加载到该对象中
    tree = html.fromstring('./test.html')
    print(tree)

