import requests
import os
url = 'http://placekitten.com/1000/400'
root = 'C:\\Users\\MSI-PC\\Desktop\\'
path = root + url.split('/')[-2] + '_' + url.split('/')[-1] +'.png'
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('图片保存成功')
    else:
        print('图片已存在')
except:
    print('爬取失败')
