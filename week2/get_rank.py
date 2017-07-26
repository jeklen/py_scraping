import requests
import bs4
from bs4 import BeautifulSoup

# 从网络上获取大学排名网页内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 提取网页内容中信息到合适的数据结构
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

# 利用数据结构展示并输出结果
def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    #print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format("排名", "学校名称", "省市", "高被引学者"))
    for i in range(num):
        u = ulist[i]
        #print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format(u[0], u[1], u[2], u[3]))
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    print("Suc" + str(num))

def main():
    uinfo = []
    url = "http://zuihaodaxue.cn/dingjianrencaipaiming2017.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
if __name__ == '__main__':
    main()