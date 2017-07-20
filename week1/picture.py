import requests

try:
    path = "C:\\Users\zhql0\Pictures\shishi1.jpeg"
    url = "http://img3.duitang.com/uploads/item/201503/29/20150329175812_cJs4H.jpeg"
    r = requests.get(url)
    r.raise_for_status()
    with open(path, 'wb') as f:
        f.write(r.content)
    f.close()
except:
    print("爬取失败")

