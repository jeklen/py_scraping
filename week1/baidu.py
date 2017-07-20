import requests

try:
    kv = {'wd':'Python'}
    r = requests.get("http://www.baidu.com/s", params=kv)
    r.raise_for_status()
    print(r.request.url)
    print(r.text[1000:2000])
except:
    print("爬取失败")