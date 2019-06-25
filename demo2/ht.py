# -*- coding:utf-8 -*-
import itchat
import datetime

itchat.login()
friendList = itchat.get_friends(update=True)[1:]
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
todayfile = open(str(today)+".txt", 'w',encoding='utf-8')
yesterdayfile = open(str(today-oneday)+".txt", 'r',encoding='utf-8')
texts=yesterdayfile.readlines()
for friend in friendList:
    flag=False
    for text in texts:
        # if(text.split("\t").__len__()>1):
            text = text.replace("\n", "")
            # print(text.split("\t")[0]+"\t"+friend['UserName'])
            if(str(text.split("\t")[0])==str(friend['AttrStatus'])):
                flag=True
                print(str(friend['AttrStatus'])+str(text.split("\t")[0]))
                break
    if(not flag):
        todayfile.writelines(str(friend['AttrStatus'])+"\t"+friend['RemarkName']+"\n")
    #     print("%s , %s" % (friend['UserName'],friend['RemarkName'] or friend['NickName']))
    # print("%s , %s ,%s" % (friend['HeadImgUrl'],friend['AttrStatus'] , friend['NickName']))
yesterdayfile.close()
todayfile.close()