# -*- coding:utf-8 -*-
import itchat
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


#此时稍微等一会，会跳出一个二维码，用手机微信扫描登录即可
itchat.login()
#friends里面就是你的好友信息啦，一共有36个字段，包括昵称、你的备注、性别、地区、签名、头像地址等等
friends = itchat.get_friends(update=True)
df_friends = pd.DataFrame(friends)
#性别统计，0是未知，1是男生，2是女生
Sex_count = df_friends['Sex'].value_counts()
plt.figure(figsize=(16,8)) #设置图片大小
labels = ['male','female','unknown']
colors = ['red','yellowgreen','lightskyblue']
#画性别分布饼图
plt.pie(Sex_count,colors=colors,labels=labels,autopct = '%3.1f%%',startangle = 90,pctdistance = 0.8)
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.legend(loc='left')
# plt.show() #这个注释打开，下面无法保存图片
plt.savefig('好友性别比例.jpg')

'''获取好友的省份和地区分布'''
Province = df_friends.Province
Province_count = Province.value_counts()
#有一些好友地理信息为空，过滤掉这一部分人
Province_count = Province_count[Province_count.index!='']
df_province =DataFrame(Province_count)
df_province.to_csv('省份分布.csv',encoding='utf-8')

City = df_friends.City
City_count = City.value_counts()
City_count = City_count[City_count.index!='']

#统计好友基本信息
number_of_friends = len(friends)
NickName = friends[0]['NickName'] #获取自己的昵称
file_name_all = NickName+'_basic_inf.txt'

with open(file_name_all,'w') as f:
    f.write('你共有%d个好友,其中有%d个男生，%d个女生，%d未显示性别。\n\n' %(number_of_friends, Sex_count[1], Sex_count[2], Sex_count[0]))

    f.write('你的朋友主要来自省份：%s(%d)、%s(%d)和%s(%d)。\n\n' %(Province_count.index[0],Province_count[0],Province_count.index[1],
     Province_count[1],Province_count.index[2],Province_count[2]))

    f.write('主要来自这些城市：%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)和%s(%d)。'%(City_count.index[0],City_count[0],City_count.index[1],
     City_count[1],City_count.index[2],City_count[2],City_count.index[3],City_count[3],City_count.index[4],City_count[4],City_count.index[5],City_count[5]))