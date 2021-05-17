import re
subclassFeaturesTmp=(['高考数学90天冲刺复习规划','高考语文90天冲刺复习规划'],['4月13日 周一 22:00-22:30 邓诚 [已结束]','4月14日 周二 22:00-22:30 殷丽娜 [已结束]'])
tmp=subclassFeaturesTmp
reg=r'(\S+)\s\S+\s\S+\s(\S+)\s\S+'
res_html_teacher=[];res_html_time=[]
for i in tmp[1]:
    tmp1=re.findall(reg,i)
    tmp1_teacher=tmp1[0][1]
    tmp1_time=tmp1[0][0]
    print(type(tmp1_teacher))
    res_html_teacher.append(tmp1_teacher)
    res_html_time.append(tmp1_time)
#print(res_html_teacher)
tmp=list(zip(tmp[0],res_html_time,res_html_teacher))
subclassFeaturesTmp=tmp
print(subclassFeaturesTmp)