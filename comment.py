import re
import urllib.request
import random

# 对评论区用户抽奖

users_list = list()
users_set = set()

# 动态下面的评论总共有2页
page = 2
for i in range(page):
    # 动态评论的接口
    url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=' + str(
        i) + '&type=11&oid=80291703&sort=2&_=1593927088823'
    # 代理用户进行浏览器伪装
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    html = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(html).read().decode('utf-8')

    users = re.findall(r'"member":{"mid":"(.*?)","uname":"(.*?)"', data, re.S)
    for user in users:
        users_list.append(user)

# 去重
users_set = set(users_list)
users_list = list(users_set)

print("评论的用户有 " + str(users_list.__len__()) + " 个: " + str(users_list))

index = random.randint(0, users_list.__len__() - 1)

print("\n\n恭喜中奖粉丝: " + str(users_list[index]))
