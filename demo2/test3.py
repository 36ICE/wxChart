# -*- coding:utf-8 -*-
import jieba,re,itchat
import numpy as np
from collections import defaultdict
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd


#此时稍微等一会，会跳出一个二维码，用手机微信扫描登录即可
itchat.login()
#friends里面就是你的好友信息啦，一共有36个字段，包括昵称、你的备注、性别、地区、签名、头像地址等等
friends = itchat.get_friends(update=True)
df_friends = pd.DataFrame(friends)
Signatures = df_friends.Signature
regex1 = re.compile('<span.*?</span>') #匹配表情
regex2 = re.compile('\s{2,}')#匹配两个以上占位符。
#用一个空格替换表情和多个空格。
Signatures = [regex2.sub(' ',regex1.sub('',signature,re.S)) for signature in Signatures]
Signatures = [signature for signature in Signatures if len(signature)>0] #去除空字符串
text = ' '.join(Signatures)
wordlist = jieba.cut(text, cut_all=False)

def statistics(lst) :
    dic = {}
    for k in lst:
        if not k.decode('utf-8') in dic :
            dic[k.decode('utf-8')] = 0
        dic[k.decode('utf-8')] +=1
    return dic

worddic = statistics(wordlist)

coloring = np.array(Image.open("./xiaodong.jpg"))#词云的背景和颜色，需要提前自己找好
my_wordcloud = WordCloud(background_color="white", max_words=2000,
              mask=coloring, max_font_size=200, random_state=8, scale=2,
              font_path="./songti.otf").generate_from_frequencies(worddic)

image_colors = ImageColorGenerator(coloring)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
my_wordcloud.to_file('签名分词.png')
#---------------------------------------------------
'''换一种词云产生方式，将关键词放大比例显示'''
word_space_split = ' '.join(wordlist)
coloring = np.array(Image.open("./xiaodong.jpg")) #词云的背景和颜色。这张图片在本地。
my_wordcloud = WordCloud(background_color="white", max_words=2000,
             mask=coloring, max_font_size=60, random_state=42, scale=2,
             font_path="./songti.otf").generate(word_space_split)

my_wordcloud.to_file('关键词签名分词.jpg') #保存图片

#--------------------------------------昵称云图-------------------------------------------------------
Nicknames = df_friends.NickName
regex1 = re.compile('<span.*?</span>') #匹配表情
regex2 = re.compile('\s{2,}')#匹配两个以上占位符。
#用一个空格替换表情和多个空格。
Nicknames = [regex2.sub(' ',regex1.sub('',nickname,re.S)) for nickname in Nicknames]
Nicknames = [nickname for nickname in Nicknames if len(nickname)>0] #去除空字符串
text_nicknames = ''.join(Nicknames)
a = re.compile(' ')
text_nicknames = a.sub('',text_nicknames)

def save_chinese(text):
    text = text.decode('utf-8')
    a = re.compile(u"[\u4E00-\u9FA5]+")
    text = a.findall(text)
    text=''.join(text)
    return text

text_nicknames = save_chinese(text_nicknames)

def get_count(Sequence):
    counts = defaultdict(int) #初始化一个字典
    for x in Sequence:
        counts[x] += 1

    return counts

nickname_count = get_count(text_nicknames)
#nickname_count_s = sorted(nickname_count.iteritems(), key=lambda d:d[1], reverse = True)
coloring = np.array(Image.open("./xiaodong.jpg"))#词云的背景和颜色，需要提前自己找。
nm_wordcloud = WordCloud(background_color="white", max_words=2000,
               mask=coloring, max_font_size=200, random_state=8, scale=2,
               font_path="./songti.otf").generate_from_frequencies(nickname_count)

# image_colors = ImageColorGenerator(coloring)
#plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(nm_wordcloud)
plt.axis("off")
plt.show()
nm_wordcloud.to_file('昵称云图.png')