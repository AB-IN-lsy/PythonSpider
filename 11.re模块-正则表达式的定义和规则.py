#正则表达式的规则定义
import re


#普通字符
vars = 'ilovelby'

reg='lby'

res=re.search(reg,vars).group()
print(res)

#转义字符 \\w \\W\ \\d \\D \\s \\S
vars='ilove521you'
reg='\w' # 代表单个字母，数字，下划线。
reg='\W' # 代表单个非字母数字下划线。
reg='\d' # 代表单个数字。
reg='\D' # 代表单个非数字。
reg='\s' # 代表单个的空格符或制表符
reg='\S' # 代表单个的非空格符或制表符
reg='\w\w\w\w' #连续四个，也可组合使用

res=re.search(reg,vars).group()
print(res)


#特殊字符 . * + ? {} [] () ^ $
vars='ilove521you hello'
reg='.' # 代表单个的任意字符，除了换行符\n
reg='.*'# * 代表匹配次数 任意次数(包括0) ，如果.一开始没有匹配到，那就没有；如果.中途没有匹配到，就把之前符合的返回
reg='\w+'# + 代表匹配次数，至少匹配一次，匹配一次之后就和*语法相同 ilove521you
reg='\w+?' # ? 拒绝贪婪，前面的匹配规则只要达成则返回 i
reg='\w*?' # 就直接返回没有，因为0也是任意次数，0已经达成了
reg='\w{4}'# 代表必须匹配次数n，{n}；{n,m} 两个数字时，表示必须匹配的区间次数
reg='[a-z]+'#[] 代表字符的范围，[a-z,A-Z] 两个范围时。
reg='\w+(\d{3})' # () 代表子组，括号中的表达式首先作为整个正则的一部分，另外会把符合小括号中的内容单独提取一份，就是存在一个元组里
#res=re.search(reg,vars).groups()
#print(res) ('521',)

vars='15305438198' 
#定义一个匹配手机号的正则表达式
reg='^1\d{10}8$' # ^代表开头(如例子，必须是1 ，匹配9个(不算开头)       $代表结尾,(匹配长度不算结尾)，整个串就结尾了
reg='^1\d{3}5\d{6}' #5前面不用加^,这里代表，从1匹配完三个后，必须从5开始匹配
res=re.search(reg,vars).group()
print(res)


#正则模式 re.I 不区分大小写
vars='iloveYOU'
reg='[a-z]{4,8}'
res=re.search(reg,vars,re.I)
print(res.group())