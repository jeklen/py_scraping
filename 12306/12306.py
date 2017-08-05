#!/usr/bin/env python
import urllib2
import ssl
from json import loads

ssl._create_default_https_context = ssl._create_unverified_context
def getList():
    html = urllib2.urlopen('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-08-17&leftTicketDTO.from_station=VRH&leftTicketDTO.to_station=AOH&purpose_codes=ADULT').read()
    print(html)
    dict = loads(html)
    print(type(dict))

getList()
