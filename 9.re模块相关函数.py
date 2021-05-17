#re模块相关函数
import re
'''
re.match() 函数
    功能：从头开始匹配，要么第一个就符合要求，要么不符合,匹配成功则返回Match对象，否则返回None，可以使用group()方法获取返回的数据
re.search()
    功能：从开头到结尾进行搜索式 匹配，开头可以不是头，要么第一个就符合要求，要么不符合,匹配成功则返回Match对象，否则返回None，可以使用group()方法获取返回的数据
re.findall()
re.finditer()
re.sub()
'''
vars='iloveyou521tosimida'
reg='ilo'


# 调用正则match 函数方法
res=re.match(reg,vars) #None(因是从头开始匹配 )
print(res) #这个为迭代器
print(res.group()) #返回当前结果
print(res.span()) #返回下标范围


#search 
res=re.search(reg,vars)
print(res)
print(res.group())
print(res.span())