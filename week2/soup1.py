# 理解Beautiful Soup库，是解析，遍历，维护标签树的功能库
# Beautiful库的解析器可以为：bs4，lxml（可写lxml，xml），html5lib
# Beautiful Soup类有5种基本元素
# 1. Tag:标签
# 2. Name:标签的名字
# 3. Attributes:标签的属性
# 4. NavigableString:标签内非属性字符串
# 5. Comment:标签内字符串的注释部分
from bs4 import BeautifulSoup

newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
print(newsoup.b.string)
print(type(newsoup.b.string))

print(newsoup.p.string)
print(type(newsoup.p.string))