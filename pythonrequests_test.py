import requests as r
def getHtml(url):
    try:
        h = r.get(url, timeout = 30)
        h.raise_for_status()
        h.encoding = h.apparent_encoding
        return h.text
    except:
        return "请求异常"
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHtml(url))
