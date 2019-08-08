import requests
########################请求代理网页—普通请求########################
#定义请求函数
def use_requests(url):
    headers = { "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36" }
    response = requests.get(url, headers=headers)#设置响应头并请求
    response.encoding = "utf-8"#设置编码
    data = response.text #以文本的形式返回
    return data
#调用
#r = use_requests("http://www.xicidaili.com")

########################根据关键字获取百度信息 - (带参请求)########################
#定义根据关键字获取百度信息的函数
def req_key_get_data(key):
    #订制头部信息
    headers = { "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36" }
    #请求的url
    url = "http://www.baidu.com/s"
    #参数会自动编码处理
    payload = { "wd" : key }
    #请求
    r = requests.get(url, params=payload , headers=headers)
    #写入文件
    with open("yin.html", "wb") as f:
        f.write(r.content)
#调用
#req_key_get_data("pyhon")
#print("执行成功!")

########################请求博客园文章 - 代理使用########################
def req_get_cnblogs_proxy(url):
    #订制头部信息
    headers = { "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36" }
    #代理参数：这里需要注意的是由于代理是使用免费的，因此有效期可能只有一分钟左右
    proxies = {
        "http": "183.159.94.214:18118",
        "https": "183.159.94.214:18118",
    }
    try:
        #请求
        r = requests.get(url, headers=headers, proxies=proxies)
        r.encoding = "utf-8" #编码
        data = r.text
        return data

    except requests.exceptions.ConnectTimeout as e: #异常捕获和处理
        return "链接超时..."
    except requests.exceptions.ProxyError as e:
        return "代理异常..."
    except: 
        return "请求异常..."
#调用
#url = "https://www.cnblogs.com/changyinlu/p/5469181.html"
#response = req_get_cnblogs_proxy(url)
#print(response)

########################中国开源社区的登陆 - Post 请求########################
##订制头部信息
headers = { "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36" }
s = requests.Session() #创建 Session 对象

def request_post_netunix(url):
    #请求参数
    payload = {'username': 'feiniuchongtian', 'password': 'aA123456'}
    #post请求
    r = s.post(url, data=payload, headers=headers)
    #写入文件中
    with open("lcy.html", "wb") as f:
        f.write(r.content)
        
#请求登录成功后在页面的其中一个链接 : http://bbs.chinaunix.net/home.php?mod=space&do=pm
def request_get_netunix(url):
    #get 请求
    r = s.get(url, headers=headers)
    #写入文件中
    with open("yin.html", "wb") as f:
        f.write(r.content)
# #调用
#url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LrIPH"
#request_post_netunix(url)#登录
#url2 = "http://bbs.chinaunix.net/home.php?mod=space&do=pm"
#request_get_netunix(url2)
#print("操作成功...")
