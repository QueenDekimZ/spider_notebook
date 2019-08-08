import requests
import time
def GetHtmlText(url, i):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('第{}次爬取成功'.format(i))
        return r.text
    except:
        print('第{}次爬取产生异常。'.format(i))
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    start = time.perf_counter()
    print('开始爬取网站：{}'.format(url))
    for i in range(1,101):
        GetHtmlText(url, i)
    spend = time.perf_counter() - start
    print('爬取100次用时：{}秒'.format(spend))
