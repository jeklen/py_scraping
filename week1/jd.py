import requests

try:
    r = requests.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.1.ebb2eb2psAiQU&id=44647145901&cm_id=140105335569ed55e27b&abbucket=4")
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print("爬取失败")