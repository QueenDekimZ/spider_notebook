import urllib.request

reponse = urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img = reponse.read()

with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
