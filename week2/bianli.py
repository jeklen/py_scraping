# 下行遍历
# .contents  返回子列表
# .children(子节点) .descendants(子孙节点)    返回迭代类型
# 上行遍历
# .parent
# .parents
# 平行遍历
# .next_sibling .previous_sibling   返回列表
# .next_siblings .previous_siblings 返回迭代类型
import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.head)

#for child in soup.body.children:
#    print(child)
