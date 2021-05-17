import requests
url='https://fanyi.baidu.com/sug' #用的是post请求,（得回车一下）

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

#post发送的数据
s=input()
data={'kw':s}# Form Data 里要求是kw

#发送请求
res=requests.post(url=url,headers=headers,data=data)

#接受返回数据
code= res.status_code
if code ==200 :
    print("请求成功")
    data=res.json() #是一个字典，一个个列表
    if data['errno']==0:
        print('响应成功')
        #print(data)
        print(data['data'][0]['k'])
        v=data['data'][0]['v']
        print(v.split(';')[-2].strip())

#print(res.text)
#print(res.json())#用json接受