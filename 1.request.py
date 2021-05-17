import requests
url='https://www.baidu.com/'

#get请求
res=requests.get(url=url)

#获取响应结果
print(res)#<Respnse [200]>
print(res.content) #b''二进制文本流
print(res.text) #获取响应结果
print(res.headers) #响应头信息
print(res.status_code)  #请求状态码 200
print(res.url) #请求的url地址
print(res.request.headers) #请求的头信息
print(res.encoding) #默认的编码方式为 'ISO-8859-1'
#请求是你发给服务器的东西，响应是服务器发给你的东西

res.encoding = 'utf-8'
print(res.text) #更改完成，返回内容的中文字符可以正常显示了