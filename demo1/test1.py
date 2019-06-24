import itchat

itchat.auto_login()

#给文件助手发消息
itchat.send('Hello, filehelper', toUserName='filehelper')

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login()
itchat.run()