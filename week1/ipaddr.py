import requests

try:
    url = "http://www.ip138.com/ips138.asp?ip="
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-1500:-1000])
except:
    print("爬取失败")