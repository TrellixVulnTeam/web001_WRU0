#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__="Alan"
import os
import sys
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
file_dir =os.path.dirname(os.path.abspath(__file__))
file_name = 'city.json'
file = file_dir+os.sep+file_name
Date =time.strftime('%Y.%m.%d')
city_name = {}
with open(file, 'r', encoding='utf-8') as f:
    # citys_json = f.read()
    citys_json = json.loads(f.read())
    for i in citys_json:
        if '市' in i.get('name'):
            city = i.get('name').split('市')[0]
            city_name[city] = [i.get('log'), i.get('lat')]
        elif '省' in i.get('name'):
            city = i.get('name').split('省')[0]
            city_name[city] = [i.get('log'), i.get('lat')]
        elif '壮族自治区' in i.get('name'):
            city = i.get('name').split('壮族自治区')[0]
            city_name[city] = [i.get('log'), i.get('lat')]
        elif '维吾尔自治区' in i.get('name'):
            city = i.get('name').split('维吾尔自治区')[0]
            city_name[city] = [i.get('log'), i.get('lat')]
        elif '回族自治区' in i.get('name'):
            city = i.get('name').split('回族自治区')[0]
            city_name[city] = [i.get('log'), i.get('lat')]
        elif '中国' in i.get('name'):
            city = i.get('name').split('中国')[1]
            city_name[city] = [i.get('log'), i.get('lat')]
        for k in i.get('children'):
            #print(k.get('name'),k.get('log'),k.get('lat'))
            if k.get('name') not in city_name:
                city_name[k.get('name')] = [k.get('log'), k.get('lat')]
        #print(i.get('children'))  # .get('name'),i.get('children').get('log'),i.get('children').get('lat'))
        #city_name[city] = [i.get('log'),i.get('lat')]
        #print(i.get('name'),i.get('log'),i.get('lat'))
        #print(i.get('name'))
#print(len(city_name))
print(city_name)