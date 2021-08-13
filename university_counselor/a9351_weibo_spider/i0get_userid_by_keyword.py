import urllib.request
from urllib import parse
 
from bs4 import BeautifulSoup
 
 
# 微博根据用户名查找userId
 
userid_list = []
# userName 用户名
# pageNum 查询页数，每页20个数据。 默认为第一页值为1，第二页值为2，以此类推。
def getUserId(userName, pageNum):
    # 用户名需要URL编码后
    # html_doc = "https://s.weibo.com/user/&nickname=" + parse.quote(userName) + "&page=" + pageNum
    html_doc = "https://s.weibo.com/user?q=" + parse.quote(userName) + "&Refer=weibo_user"
    req = urllib.request.Request(html_doc)
    webpage = urllib.request.urlopen(req)
    html = webpage.read()
    soup = BeautifulSoup(html, 'html.parser')  # 文档对象
    if soup:
        print("找到html")
    # 第一步：抓取a标签
    # <a class="name" href="//weibo.com/u/5288987897" 
    # suda-data="key=tblog_search_weibo&amp;value=seqid:157406704247901067764|type:3|
    # t:0|pos:1-0|q:|ext:mpos:1,click:user_name" target="_blank">
    # 暴烈甜心<em class="s-color-red">小</em><em class="s-color-red">鳄鱼</em>毛毛</a>
    for a in soup.find_all('a', class_='name'):
        if a:
            # 第二步：抓取a标签中用户名
            rpuserName = a.get_text()
            print("搜到用户名=" + rpuserName)
            # 第三步： 判断是否有该用户，如果有，获取该用户userId
            # if a.get_text(strip=True) == userName:
            print("匹配到该用户")
            print("用户个人主页链接=" + a['href'])
            # 第四步：提取userId，然后返回
            userUrl = a['href'].split("/")
            print(userUrl)
            if userUrl and len(userUrl) > 0:
                userId = userUrl[len(userUrl) - 1]
                # return "userId=" + userId
                print("userId=" + userId)
                userid_list.append(userId)
            else:
                # return "userID抓取失败"
                print('serID抓取失败')
            # break
        else:
            # return "没有查找到a标签"
            print('没有查找到a标签')
    else:
        # return "没有找到数据"
        print('没有找到数据')
 
 
if __name__ == "__main__":
    userName = "腾讯"
    for i in range(1, 5):
        getUserId(userName, str(i))
    print(len(userid_list), userid_list)
    
