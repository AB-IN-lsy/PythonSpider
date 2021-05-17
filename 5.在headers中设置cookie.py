import requests
#url='http://www.lmonkey.com/'
url='https://www.lmonkey.com/my/order' #服务器拒绝请求，拒绝python-request,所以定义请求头信息

#定义请求头信息
"""
1.找个网页点检查
2.刷新网页
3.找到network-nn-headers-User-Agent
"""
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'cookie':'Hm_lvt_676e52e2eddd764819cab505b21e9ee8=1593066230; UM_distinctid=172ea2595ad48-0b28d6995dd9b6-4313f6a-144000-172ea2595aeade; CNZZDATA1277679765=845925555-1593065656-https%253A%252F%252Fwww.baidu.com%252F%7C1593065656; qimo_seosource_ad8e1ca0-2091-11ea-af9d-6523a0f144a7=%E7%99%BE%E5%BA%A6%E6%90%9C%E7%B4%A2; qimo_seokeywords_ad8e1ca0-2091-11ea-af9d-6523a0f144a7=; href=https%3A%2F%2Fwww.lmonkey.com%2F; accessId=ad8e1ca0-2091-11ea-af9d-6523a0f144a7; XSRF-TOKEN=eyJpdiI6ImFydFV6UCt2Und5Y2E4aXl1ZlpJb2c9PSIsInZhbHVlIjoibFo5T1wvekpBTVwvdzdPank1eGpVM0pJelVFU2hDRzd0ajk5OVwvQjFvUThSTm4xU21UY3pNWHRWQjh4bDRyK0l5VyIsIm1hYyI6IjVkYTZmYWViMTM1NGM4YjM1MDRkOTE5NThmODg4NDViNGNmYThlY2I0MzVjZTdjOTQwOGE4NjgxMzY5OTE2YzMifQ%3D%3D; _session=eyJpdiI6IkVRV0lXMmdzSFdQOW9yQjZXeWxxenc9PSIsInZhbHVlIjoiOVpLMHUwVEU4cmVnMFBkeHJVMlwvTGw0V2xLR0JKUks5blNTQnN6YnVJajhYVGpwS0J3ZGRCbjN4SldXRjYyUGYiLCJtYWMiOiJlMWQ1YWJlYTkyMmM1NjY1YjQyNWQ1OTczNzQzNjNhNjE5NzZhMTc0MzliMDU5NDVkMGMzZGMzYjYyZjBjMjMwIn0%3D; Hm_lpvt_676e52e2eddd764819cab505b21e9ee8=1593066389; pageViewNum=10'
}


res=requests.get(url=url,headers=headers)


#获取响应状态码
code=res.status_code
print(code)

#响应成功后把响应的内容写入文件
if code== 200:
    with open('./test.html','w',encoding='utf-8') as fp:
        fp.write(res.text)
#Ctrl + F 搜索