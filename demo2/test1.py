# -*- coding:utf-8 -*-
import itchat
from pandas import DataFrame


itchat.login()
friends = itchat.get_friends(update=True)[0:]
male = female = other = 0
for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

total = len(friends[1:])
malecol = round(float(male) / total * 100, 2)
femalecol = round(float(female) / total * 100, 2)
othercol = round(float(other) / total * 100, 2)
print('男性朋友：%.2f%%' % (malecol) +
      '\n' + '女性朋友:%.2f%%' % (femalecol) +
      '\n' + '性别不明的好友：%.2f%%' % (othercol))

# 使用echarts，加上这段
from echarts import Echart, Legend, Pie #pip install echarts-python

chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
chart.use(Pie('WeChat',
              [{'value': male, 'name': u'男性 %.2f%%' % malecol},
               {'value': female, 'name': u'女性 %.2f%%' % femalecol},
               {'value': other, 'name': u'其他 %.2f%%' % othercol}],
              radius=["50%", "70%"]))
chart.use(Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()

def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

NickName = get_var('NickName')#昵称
Sex = get_var('Sex')#性别
Province = get_var('Province')#省份
City = get_var('City')#城市
Signature = get_var('Signature')#签名

data = {'NickName': NickName,
        'Sex': Sex,
        'Province': Province,
        'City': City,
        'Signature': Signature
        }

frame = DataFrame(data)
frame.to_csv('data.csv', index=True, encoding="utf_8_sig")


# 使用echarts，加上这段
from echarts import Echart, Legend, Pie

chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
chart.use(Pie('WeChat',
              [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
               {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
               {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
              radius=["50%", "70%"]))
chart.use(Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()


