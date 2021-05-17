'''
re.findall()
    按照正则表达式的规则在字符串中匹配元素，结果返回一个列表，如果没有则返回空列表
re.finditer()
    返回一个迭代器
re.sub()
    搜索替换功能，按照正则表达式的规则，在字符串中找到需要被替换的字符串
    参数：
    pattern：正则表达式的规则
    repl:替换后的字符串
    string:被替换的原始字符串
compile()
    可以直接正则表达式定义为正则对象，使用正则对象操作
'''
import re
vars='iloveyou521tosimida511'
reg='\d{3}'#可以三个函数为一组 ['521', '511']
#reg='\d{2}' ['52', '51']
#reg='\d{4}' []


res=re.findall(reg,vars)
print(res)


res=re.finditer(reg,vars)
print(list(res)) #有几个返回几个 [<re.Match object; span=(8, 11), match='521'>, <re.Match object; span=(19, 22), match='511'>]


#替换成其它
res=re.sub(reg,'AAA',vars)#iloveyouAAAtosimidaAAA
print(res)


#直接定义正则表达式对象
reg= re.compile('\d') #取代re,相当于不用传正则对象
res= reg.findall(vars)
print(res)