"""会员宝总计 从简书获取账单
刷卡机TX后的钱用来理财了，但是刷多了会很凌乱，需要记账和总结
"""
from bs4 import BeautifulSoup
import requests

res = requests.get("http://www.jianshu.com/p/ed677b95c777")
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')

source = soup.find_all(class_='show-content')
#print(source)
"""[] ：可变的list  （）：tuple 不可变list"""
orderList = []

print("刷卡时间     消费金额")
for tag in source:
    litags = tag.find_all('li')
    for li in litags:
        value = str(li).split('>')[1].split('<')[0];
        print(value.split(" ")[0]+"     "+value.split(" ")[2])
        map = {"day": value.split(" ")[0], "pay": float(value.split(" ")[2])}
        orderList.append(map)


"""费率"""
hybfl = 0.0055


def cost():
    costmoney = 0
    for order in orderList:
        costmoney = costmoney + order.get("pay") * hybfl + 3
    return costmoney


def allmoney():
    getmoney = 0
    for order in orderList:
        getmoney = getmoney + order.get("pay")
    return getmoney


print("总费率:%s   到账金额:%s" % (round(cost(),2), round(allmoney() - cost(),2)))
