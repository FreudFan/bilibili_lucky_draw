import re
import urllib.request
import random

# 对转发了动态用户抽奖

users_forward_list = list()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}

# 转发用户列表接口
url = 'https://api.vc.bilibili.com/dynamic_repost/v1/dynamic_repost/repost_detail?dynamic_id=408392308284261525'
html = urllib.request.Request(url=url, headers=headers)
data = urllib.request.urlopen(html).read().decode('utf-8')
# 使用正则筛选用户Id和昵称
forward_users = re.findall(r'"user_profile":{"info":{"uid":(.*?),"uname":"(.*?)"', data, re.S)

for user in forward_users:
    users_forward_list.append(user)

print("转发的用户有 " + str(users_forward_list.__len__()) + " 个: " + str(users_forward_list))

index = random.randint(0, users_forward_list.__len__() - 1)

print("\n\n恭喜中奖粉丝: " + str(users_forward_list[index]))
