import requests
import os

url = 'https://img.alicdn.com/imgextra/i1/1886345017/TB2nBnFXaPeFuJjy0FlXXbdcpXa_!!1886345017.jpg'
#root = 'd://mycode//py_scraping//download//'
root = './/download//'
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')