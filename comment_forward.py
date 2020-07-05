import re
import urllib.request
import random

# 对转发+评论用户抽奖

users_forward_list = list()
users_comment_list = list()
users_final_list = list()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}

# 获取动态评论用户
# 动态下面的评论总共有1页
page = 2
for i in range(page):
    # 动态评论的接口
    url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=' + str(
        i) + '&type=11&oid=80291703&sort=2&_=1593927088823'
    html = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(html).read().decode('utf-8')
    comment_users = re.findall(r'"member":{"mid":"(.*?)","uname":"(.*?)"', data, re.S)

    for user in comment_users:
        users_comment_list.append(user)

# 去重
users_comment_list = list(set(users_comment_list))
print("评论的用户有 " + str(users_comment_list.__len__()) + " 个：" + str(users_comment_list))

# 转发信息接口
url = 'https://api.vc.bilibili.com/dynamic_repost/v1/dynamic_repost/repost_detail?dynamic_id=408392308284261525'
html = urllib.request.Request(url=url, headers=headers)
data = urllib.request.urlopen(html).read().decode('utf-8')

forward_users = re.findall(r'"user_profile":{"info":{"uid":(.*?),"uname":"(.*?)"', data, re.S)
for user in forward_users:
    users_forward_list.append(user)

print("转发的用户有 " + str(users_forward_list.__len__()) + " 个: " + str(users_forward_list))

# 转发+评论用户
for forward in users_forward_list:
    for comment in users_comment_list:
        if forward == comment:
            users_final_list.append(forward)

print("转发+评论的用户有 " + str(users_final_list.__len__()) + " 个: " + str(users_final_list))

index = random.randint(0, users_final_list.__len__() - 1)

print("\n\n恭喜中奖粉丝: " + str(users_final_list[index]))
