import requests
import re

def getHTMLText(url):
    try:
        kv = {'User-agent':'Mozilla/5.0'}
        pxs = {'http': 'http://114.99.7.122:8752',
              ' https': 'https://114.99.7.122:8752'
            }
        r = requests.get(url,headers = kv,proxies = pxs)
        r.raise_for_status() 
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("Not Found")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    f = {}
    for g in ilt:
        count = count + 1
        f[count] = g
    for i in range(1,count+1):
        for j in range(i+1, count+1):
            if f[j][0] > f[i][0]:
                temp = f[j][0]
                f[j][0] = f[i][0]
                f[i][0] = temp
                temp1 = f[j][1]
                f[j][1] = f[i][1]
                f[i][1] = temp1
            else:
                continue
    for i in range(1,count+1):
        print(tplt.format(i,f[i][0],f[i][1]))
       # print(tplt.format(count,f[count][0],f[count][1]))

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
main()
