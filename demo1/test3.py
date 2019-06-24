# coding=utf8
import itchat, time

itchat.auto_login(True)

SINCERE_WISH = u'祝%s新年快乐！'
a=itchat.get_friends(update=True)
itchat.get_chatrooms(update=True)
itchat.get_contact(update=True)

itchat.get_mps(update=True)
itchat.get_msg()


friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    # 如果是演示目的，把下面的方法改为print即可
    # itchat.send(SINCERE_WISH % (friend['DisplayName']
    #                             or friend['NickName']), friend['UserName'])
    print("%s , %s" % (friend['DisplayName'] or friend['NickName'], friend['UserName']))
    # time.sleep(.5)
