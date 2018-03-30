import requests
import bs4
from bs4 import BeautifulSoup

#定义函数 打印糗事百科段子
def print_duanzi(url):
    req = requests.get(url)
    #print(req.content.decode("utf-8"))
    soup = BeautifulSoup(req.content, 'html.parser')
    msgList = []
    for tag in soup.find_all('span'):
        if not tag.get('class') and type(tag.string)==bs4.element.NavigableString:
            msgList.append(tag.string)
    retstr = ''
    for index in range(len(msgList)-4):
        retstr = retstr + msgList[index].replace('\n\n\n', '')
    return retstr

#调用打印段子
page = 1   #页数
url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
msg = print_duanzi(url)
print(msg)