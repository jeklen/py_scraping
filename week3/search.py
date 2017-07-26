import re

match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

match = re.match(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

# 匹配的字符就相当于分隔符了，而分隔符去掉
split = re.split(r'[1-9]\d{5}', 'BIT100081 Tsu100084')
if split:
    print(split)
