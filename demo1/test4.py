# coding=utf8
import itchat, time

itchat.auto_login(True)

REAL_SINCERE_WISH = u'祝%s新年快乐！！'

chatroomName = 'Damn it bitch 410'
itchat.get_chatrooms(update=True)
chatrooms = itchat.search_chatrooms(name=chatroomName)
if chatrooms is None:
    print(u'没有找到群聊：' + chatroomName)
else:
    chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
    for friend in chatroom['MemberList']:
        friend = itchat.search_friends(userName=friend['UserName'])
        # 如果是演示目的，把下面的方法改为print即可
        # itchat.send(REAL_SINCERE_WISH % (friend['DisplayName']
        #                                  or friend['NickName']), friend['UserName'])
        print("%s , %s" % (friend['DisplayName'] or friend['NickName'], friend['UserName']))
        time.sleep(.5)