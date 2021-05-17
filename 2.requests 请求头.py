import requests
#url='http://www.lmonkey.com/'
url='http://www.xicidaili.com/nn' #服务器拒绝请求，拒绝python-request,所以定义请求头信息

#定义请求头信息
"""
1.找个网页点检查
2.刷新网页
3.找到network-nn-headers-User-Agent
"""
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}


res=requests.get(url=url,headers=headers)


#获取响应状态码
code=res.status_code

print(code)

#响应成功后把响应的内容写入文件
if code== 200:
    with open('./test.html','w',encoding='utf-8') as fp:
        fp.write(res.text)
    