import requests

keyword = 'Python'
try:
    kv_headers = {'user-agent':'Mozilla/5.0'}
    kv = {'wd':keyword}
    r = requests.get('http://www.baidu.com/s',headers = kv_headers, params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')