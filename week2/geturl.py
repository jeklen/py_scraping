import requests
import re
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

#for link in soup.find_all('a'):
#    print(link.get('href'))

#print(soup.find_all('p', 'course'))

#print(soup.find_all(id='link1'))

#print(soup.find_all(id='link'))

print(soup.find_all(id=re.compile('link')))

print(soup.find_all(string = "Basic Python"))

print(soup.find_all(string = re.compile('python')))
