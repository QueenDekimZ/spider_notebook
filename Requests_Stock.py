import requests
from bs4 import BeautifulSoup
import traceback
import os
import re

def getHTMLText(url, code='utf-8'):
##    print('3')
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = code  ##r.apparent_encoding
        return r.text
    except:
        return ""
def getStockList(lst, stockURL, stock_num):
##    print("1")
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs.get('href')
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
            if len(lst) >= stock_num:
                break
        except:
            continue
def getStockInfo(lst, stockURL, fpath):
##    print('2')
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名单':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding = 'utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前速度:{:.2f}%'.format(count*100/len(lst)),end='')
        except:
            count = count + 1
            print('\r当前速度:{:.2f}%'.format(count*100/len(lst)),end='')
##            traceback.print_exc()
            continue
def FolderAndFile_Judge(folder, file):
    if  not os.path.exists(folder):
        os.mkdir(folder)
    if os.path.exists(file):
        print('文件已存在。')
        os._exit(0)
def main():
    depth = 10
    print("Start")
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_folder = 'C://Users//MSI-PC//Desktop//RequestsTest'
    output_file = output_folder + '//BaiduStockInfo.txt'
    slist = []
    FolderAndFile_Judge(output_folder, output_file)
    getStockList(slist, stock_list_url, depth)
    getStockInfo(slist, stock_info_url, output_file)
if __name__ == '__main__':
    main()
