import requests
r = requests.get("http://python123.io/ws/demo.html")
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, "lxml")

'''
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
</body></html>
'''

#soup.tag 返回第一个tag内容
print(soup.title)
print(soup.a)
#标签名

print(soup.a.parent.name) #p 获取a的父亲的名字
print(soup.a.parent.parent.name) #body

tag_a = soup.a
print(tag_a.attrs) #字典 {'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
print(tag_a.attrs['class']) #['py1']

print(tag_a.string) # 内容 Basic Python
print(type(tag_a.string)) #<class 'bs4.element.NavigableString'>

print(soup.head.contents) #返回儿子结点信息,为列表
#[<title>This is a python demo page</title>]
print(soup.body.contents) #返回儿子结点信息
print(soup.body.contents[1]) 

print(soup.title.parent) #返回父亲结点信息
#<head><title>This is a python demo page</title></head>
#遍历节点时 if *** is None 不打印

#平行遍历发生在同一个父节点下的各节点间


print(soup.prettify()) #美化的html文档

for link in soup.find_all('a'):
    print(link['href'])
#找所有标签为a的链接

