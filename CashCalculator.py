import math
"""这是我YY消费贷（朋友的POS机刷卡TX）或汽车金融买BMW的利息对比。
嗯。虽然目前还是负债。梦想还是要有的，万一见鬼了呢"""



allmoney = 30000 #假设消费贷款三万
time = 12 #刷一半留一半.一年12次
fl = 0.0055 #刷卡费率0.55%
year = 1 #周期一年
sxf = 3 #手续费3元


def cashFrom1Credit():

    allCost = allmoney*fl*year*time + sxf*time

    getfl = 0.04 #理财4%
    getallday = 28-12 #理财时间


    allget = allmoney*getfl/365*getallday*time;
    return allCost-allget;

print(cashFrom1Credit())


def cashFromBMW():
    fl = 0.0588
    allcost = allmoney*0.0588
    return allcost

print(cashFromBMW())
