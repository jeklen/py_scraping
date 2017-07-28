import re

# re库默认的是最大匹配
# 在操作符后面加一个问号，就变成了最小匹配
# *?    +?      ??      {m, n}?
match = re.search(r'PY.*N', 'PYANBNCNDN')
print(match.group(0))

match = re.search(r'PY.*?N', 'PYANBNCNDN')
print(match.group(0))