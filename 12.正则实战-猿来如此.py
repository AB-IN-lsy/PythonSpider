'''
数据地址：'https://www.lmonkey.com/ask'
数据字段：问题，时间，作者
'''
import requests,re,json
url = 'https://www.lmonkey.com/ask'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

res= requests.get(url=url,headers=headers)

if res.status_code==200:
    #获取返回数据，进行数据解析
    res_html=res.text
    with open('./res.html','w',encoding='utf-8') as fp:
        fp.write(res_html)
    #<div class="topic_title mb-0 lh-180 ml-n2">【前端】学习猿地的课程列表页，怎么我在官网找不到？有老师用到的图片素材吗？<small class="float-right text-muted" data-toggle="tooltip" data-placement="top" title="" data-original-title="0个回复"><i class="fa fas fa-comments"></i>&nbsp;0</small></div>
    #定义解析问题标题的正则
    reg='<div class="topic_title mb-0 lh-180 ml-n2">(.*?)<small'
    #调用正则方法去获取问题的标题
    arr=re.findall(reg,res_html)
    #定义解析作者的正则
    reg='<strong>(.*?)</strong>'
    authorlist=re.findall(reg,res_html)
    #print(authorlist)
    #定义解析时间的正则
    reg='<span data-toggle="tooltip" data-placement="top" title="(.*?)">'
    time=re.findall(reg,res_html)
    print(time)

    #url链接
    reg='<a href="(https://www.lmonkey.com/ask/\d+)" target="_blank">' #括号框起来，返回的列表就只有小括号里的了
    v_url=re.findall(reg,res_html)
    #print(v_url)

    data=list(zip(arr,authorlist,time,v_url)) #打包成一个个元组,压缩数据
    #print(data)


    # 常规方法处理数据 [{} {} {} ....]
    # datalist=[]
    # for i in data:
    #     res={'title':i[0],'author':i[1],'datatime':i[2],'url':i[3]}
    #     datalist.append(res)
    # #print(datalist) 

    datalist=[{'title':i[0],'author':i[1],'datatime':i[2],'url':i[3]} for i in data]
    #print(datalist)

    #数据入库
    with open('./data.json','w',encoding='utf-8') as fp:
        json.dump(datalist,fp,ensure_ascii=False,indent=4)

