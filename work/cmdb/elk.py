#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__="Alan"
#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__="Alan"
import os
import sys
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
from elasticsearch import Elasticsearch
file_dir =os.path.dirname(os.path.abspath(__file__))
file_name = 'city_name.json'
file = file_dir+os.sep+file_name
Date =time.strftime('%Y.%m.%d')
es_connect = {
    'host':'172.19.5.158',
    'port':9200
}
es = Elasticsearch([es_connect])
def query_ip(size=10,field='geoip.ip'):
    Query_IP = {"query":
                    {"bool":
                         {"must":
                              {"range":
                                   {"@timestamp": {"gt": "now-10m"}}
                               }
                          }
                     },
                "aggs": {
                    "refer": {
                        "terms": {
                            "field": "%s" %field
                            , "size": size, "order": {
                                "_count": "desc"}
                        }
                    }
                },
                "size": 0
    }
    return Query_IP
def query_city(Size=1,ip='211.94.236.79',date_limt = 10):
    Query_City = {"query":
        {"bool":
            {
                "filter":
                    {"range":
                         {"@timestamp": {"gt": "now-%sm" %date_limt}}
                     },
                "must":
                    {"match":
                         {"geoip.ip": "%s" % ip}
                     }
            }
        },
        "size": Size
    }
    return Query_City
def run(date=Date,Date_limt=10,size=10):
    ip_data_json = es.search(index='logstash-%s'% Date,body=query_ip(size))
    ip_data_list = (ip_data_json.get('aggregations').get('refer').get('buckets'))
    city_name = {}
    ip_dict = {}
    ip_list = []
    city_dict = {}
    city_num = {}
    ip_city__num = {}
    with open(file,'r',encoding='utf-8') as f:
        #citys_json = f.read()
        citys_json = json.loads(f.read())
        for i in citys_json:
            city_name[i.get('pinyin')] = i.get('name')
    for i in ip_data_list:
        ip_dict[i.get('key')]=i.get('doc_count')
        ip_list.append(i.get('key'))
        ip_city_json = es.search(index='logstash-%s'%date, body=query_city(ip=i.get('key'),date_limt=Date_limt))
        city = ip_city_json.get('hits').get('hits')[0].get('_source').get('geoip').get('city_name')
        city_dict[i.get('key')]=city_name.get(city)
        if city_name.get(city) in city_num:
            num = ip_dict.get(i.get('key'))
            city_num[city_name.get(city)] = i.get('doc_count') + num
        elif city_name.get(city):
            city_num[city_name.get(city)] = i.get('doc_count')
        if city_name.get(city) :
            ip_city__num[i.get('key')] = {city_name.get(city):i.get('doc_count')}
    return city_num
if __name__ == '__main__':
    start_time = time.time()
    test = run()
    end_time = time.time()
    print(end_time-start_time,test)