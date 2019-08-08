import requests
from bs4 import BeautifulSoup
import bs4
def getHtmlTest(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

def printUnivList(ulist, num):
    tplt = "{0:{4}<6}\t{1:{4}<10}\t{2:{4}<10}\t{3:<10}"
    print(tplt.format("排名","学校名称","地区","总分",chr(12288)))
    for i in range(num):
          u = ulist[i]
          print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
    html = getHtmlTest(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)

if __name__ == "__main__":
    main()
    
