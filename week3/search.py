# 返回match对象
# re.search()
# re.match()
# re.finditer()
# 返回列表类型
# re.findall()  搜索字符串，以列表类型返回全部能匹配的子串
# re.split()
# 返回替换后的字符串
# re.sub()

## re库的第二种用法
# 面向对象用法，编译后的多次操作
# pat = re.compile(r'[1-9]\d{5}')
# rst = pat.search('BIT 100081')
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

split = re.split(r'[1-9]\d{5}', 'BIT100081 Tsu100084', maxsplit=1)
if split:
    print(split)

# 迭代
for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print(m.group(0))

sub_str = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 Tsu100084')
print(sub_str)
