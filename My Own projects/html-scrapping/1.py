import requests

url = 'https://www.amazon.in/'

r = requests.get(url)

fname = url.split(sep='/')
with open(fname[-2].__add__('.html') , 'wb') as f:
    f.write(r.content)