import requests


#需要请求的目标网址
url='http://www.rrys2019.com/user/user' 

#登录请求的地址
loginurl='http://www.rrys2019.com/User/Login/ajaxLogin'

#请求头
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

#如果需要爬虫程序主动记录cookie并且携带cookie，那么在使用requests之前先调用session方法
#并且使用session方法返回的对象发送请求

req=requests.session()#请求对象

#登陆请求数据
data={
'account': 'AB_IN',
'password': 'Lsy118690',
'remember': '1',
'url_back': 'http://www.rrys2019.com/user/user'
}

#用请求对象发起登陆请求
res = req.post(url= loginurl,headers=headers,data=data)

#判断状态
code=res.status_code
print(code)

if code==200:
    #发起新的请求，获取目标数据
    res=req.get(url=url,headers=headers)#这就是获取登陆成功的网页信息了,得用访问的对象进行访问，如果用request会是一个新的对象发请求
    with open('rr.html','w',encoding='utf-8') as fp:
        fp.write(res.text)

