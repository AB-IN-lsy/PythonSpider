import re
#正则表达式 re


'''
正则表达式的组成:
    普通字符： 大小写字母，数字，符号，etc
    转义字符： \\w \\W\ \\d \\D \\s \\S etc
    特殊符号：. * ？ + ^ $ [] () {}
    匹配模式：I U etc
'''

#定义字符串
vars='iloveyou521tosimida'

#定义正则表达式
reg='\\d' #代表一个数字
reg1='521'#代表一个串
#调用正则函数方法

res=re.findall(reg,vars) #相当于找里面的所有数字
#['5', '2', '1']
print(res)


res=re.findall(reg1,vars) 
#['521']
print(res)


res=re.finditer(reg1,vars) #返回一个迭代器保存了匹配对象
print(next(res))
#<re.Match object; span=(8, 11), match='521'>