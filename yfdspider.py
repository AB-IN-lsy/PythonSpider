import time,re
from lxml import etree
import json
import requests

def classTypeJudge(html): # 已完善
    '''
    自从HTML文件下载下来之后就首先要调用这个函数，用来判断是系统班课还是专题课。
    如果是专题班课special，再交给subjectJudge来判断科目，然后使用specialParse解析
    如果是系统班课systemic，再交给systemicJudge来判断科目，然后使用systemicParse解析
    '''
    if html.xpath("//h3[@class='name']/i/@class") == ['icon-systemic']:
        return 'systemic'
    else:
        return 'special'

def specialJudge(subjectLable): # 已完善
    '''
    这个函数的参数是用Xpath解析出的网页图标类的列表的第0项
    html.xpath("//h3[@class='name']/i/@class")[0]
    
    这个函数返回的是图标类对应的科目
    '''
    if subjectLable=='icon-systemic':
        return 'Systemic'
    elif subjectLable=='icon-literature':
        return '语文'
    elif subjectLable=='icon-math':
        return '数学'
    elif subjectLable=='icon-english':
        return '英语'
    elif subjectLable=='icon-physics':
        return '物理'
    elif subjectLable=='icon-chemistry':
        return '化学'
    elif subjectLable=='icon-biology':
        return '生物'
    elif subjectLable=='icon-history':
        return '历史'
    elif subjectLable=='icon-geography':
        return '地理'
    elif subjectLable=='icon-politics':
        return '政治'
    elif subjectLable=='icon-undefined':
        return '其他课程(道德与法治等)'
    elif subjectLable=='icon-ted':
        return '讲座'
    else:
        return '无法识别的课程'

def systemicJudge(title): # 已完善
    '''
    由于系统班没有标出具体科目，所以要从title里面识别

    title是标题的字符串
    返回课程科目的中文字符串
    '''
    if '语文' in title:
        return '语文'
    elif '数学' in title:
        return '数学'
    elif '英语' in title:
        return '英语'
    elif '物理' in title:
        return '物理'
    elif '化学' in title:
        return '化学'
    elif '生物' in title:
        return '生物'
    elif '政治' in title:
        return '政治'
    elif '地理' in title:
        return '地理'
    elif '文综' in title:
        return '文综'
    else:
        return '无法识别的课程'

def specialParse(html,courseId): # 待完善
    '''
    by pb&lsy
    专题课的解析函数，参数为整个页面的HTML字符串和解析的courseId

    返回一个字典，{courseId:{

        title 是课程标题

        subjectLst,subject 是为了解析课程的科目

        features 指出了课程对应的年级

        teachers 是授课教师 注意，由于页面上的授课教师最多展示3个，所以我们从每小节的标题
                 用正则表达式解析出教师名字，将真实的老师列表放在这里。

        subclassFeatures 是一个列表，这个班课有几个小节就有几个元组
                         元组是(小节标题(subclassTitle)，小节老师，小节时间YYYYMMDD)
                         小节老师和小节时间需要用正则表达式从subclassFeaturesTmp里解析
                         有可能不显示老师
    }}
    '''
    title=html.xpath("//h3[@class='name']/text()")
    subjectLst=html.xpath("//h3[@class='name']/i/@class")
    subject=specialJudge(subjectLst[0])
    features=html.xpath("//div[@class='basic-info']//p[@class='features']/text()")
    teachers=html.xpath("//ul[@class='teachers cf sm horizontal']/li//p/text()")
    subclassTitle=html.xpath("//div[@class='outline-item']//div[@class='lesson-desc']/h4/text()")
    subclassFeaturesTmp=html.xpath("//div[@class='outline-item']//div[@class='lesson-desc']/p/text()")
    detailInfo={
        'title':title[0],
        'subject':subject,
        'features':features[0],
        'teachers':teachers,
        'subclassFeatures':(subclassTitle,subclassFeaturesTmp)
    }
    tmp=detailInfo['subclassFeatures']
    reg='(\\S+)\\s\\S+\\s\\S+\\s+(.*)'
    res_html_teacher=[];res_html_time=[]
    for i in tmp[1]:
        tmp1=re.findall(reg,i)
        try:
            lst=tmp1[0][1].split()
            if len(lst)==2:
                res_html_teacher.append(lst[0])
                res_html_time.append(tmp1[0][0])
            elif len(lst)==1 and '[已结束]' in lst:
                res_html_teacher.append('无教师')
                res_html_time.append(tmp1[0][0])
            elif len(lst)==1 and '[已结束]' not in lst:
                res_html_teacher.append(lst[0])
                res_html_time.append(tmp1[0][0])
        except IndexError:
            res_html_teacher.append('无教师')
            reg1='(\\S+).*'
            tmp1=re.findall(reg1,i)
            res_html_time.append(tmp1[0])
    tmp=list(zip(tmp[0],res_html_time,res_html_teacher))
    res_html_teacher=list(set(res_html_teacher))
    detailInfo['subclassFeatures']=tmp
    detailInfo['teachers']=res_html_teacher
    res={courseId:detailInfo}
    return res

def systemicParse(html,courseId): # 待完善
    '''
    by pb
    系统班课的解析函数，参数为整个页面的HTML字符串和解析的courseId

    返回一个字典，{courseId:{

        title 是课程标题

        titleParse和subject 是为了解析课程的科目，由于系统班没有标出具体科目，所以要从title里面识别

        features 指出了课程对应的年级

        teachers 是授课教师，这里的老师直接从页面解析，因为系统班课只有1或2个老师

        subclassFeatures 是一个列表，这个班课有几个小节就有几个元组
                         元组是(小节标题(subclassTitle)，小节老师，小节时间YYYYMMDD)
                         小节老师和小节时间需要用正则表达式从subclassFeaturesTmp里解析
                         有的页面不显示具体教师，这个问题特殊对待
    }}
    '''
    title=html.xpath("//h3[@class='name']/text()")
    subject=systemicJudge(title[0])
    features=html.xpath("//div[@class='basic-info']//p[@class='features']/text()")
    teachers=html.xpath("//ul[@class='teachers cf sm horizontal']/li//p/text()")
    subclassTitle=html.xpath("//div[@class='outline-item']//div[@class='lesson-desc']/h4/text()")
    subclassFeaturesTmp=html.xpath("//div[@class='outline-item']//div[@class='lesson-desc']/p/text()")
    detailInfo={
        'title':title[0],
        'subject':subject,
        'features':features[0],
        'teachers':teachers,
        'subclassFeatures':(subclassTitle,subclassFeaturesTmp)
    }
    tmp=detailInfo['subclassFeatures']
    reg='(\\S+)\\s\\S+\\s\\S+\\s+(.*)'
    res_html_teacher=[];res_html_time=[]
    for i in tmp[1]:
        tmp1=re.findall(reg,i)
        try:
            lst=tmp1[0][1].split()
            if len(lst)==2:
                res_html_teacher.append(lst[0])
                res_html_time.append(tmp1[0][0])
            elif len(lst)==1 and '[已结束]' in lst:
                res_html_teacher.append('无教师')
                res_html_time.append(tmp1[0][0])
            elif len(lst)==1 and '[已结束]' not in lst:
                res_html_teacher.append(lst[0])
                res_html_time.append(tmp1[0][0])
        except IndexError:
            res_html_teacher.append('无教师')
            reg1='(\\S+).*'
            tmp1=re.findall(reg1,i)
            res_html_time.append(tmp1[0])
    tmp=list(zip(tmp[0],res_html_time,res_html_teacher))
    # detailInfo['teachers']=res_html_teacher
    detailInfo['subclassFeatures']=tmp
    res={courseId:detailInfo}
    return res

def main(html,courseId):
    '''
    这是一个主函数，将之前的 判断课程类型——判断科目——解析数据 串联起来
    '''
    classType=classTypeJudge(html)

    if classType=='systemic':
        res=systemicParse(html=html,courseId=courseId)
        return res

    elif classType=='special':
        res=specialParse(html=html,courseId=courseId)
        return res

if __name__=='__main__':
    # 程序入口
    # courseId='4031403'
    # with open("./src/yfdtest.html",'r',encoding='utf-8') as fp:
    #     html=etree.HTML(fp.read())
    startTime=time.time()
    reslst=[]
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54'
    }

    for courseId in range(4031403,4031404):
        url=f'https://www.yuanfudao.com/lessons/{courseId}.html'
        page=requests.get(url=url,headers=headers)
        pageHtml=page.content.decode('utf-8')
        pageHtmlTree=etree.HTML(pageHtml)
        if page.status_code==200:
            # 获取到HTML，准备解析 
            print(f'200：courseId为{courseId}的网页正在解析')  
            res=main(html=pageHtmlTree,courseId=courseId)
            reslst.append(res)
            print(f'200：***courseId为{courseId}的网页解析成功***')
        elif page.status_code==404:
            # 404是网页不存在
            print(f'404：courseId为{courseId}的网页状态404，无需解析')
        else:
            # 其他情况一般是服务器拒绝了响应
            print(f'!!!courseId为{courseId}的网页状态{page.status_code}，需要注意!!!')

    with open('./src/yfd.json','a',encoding='utf-8') as fp:
            fp.write(json.dumps(reslst,ensure_ascii=False,indent=4))
            print(f'写入了{len(reslst)}个页面')
    
    endTime=time.time()
    timeAssumption=endTime-startTime
    print(f'完成这个程序用了{timeAssumption}秒')