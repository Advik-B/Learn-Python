import requests
from bs4 import BeautifulSoup

r = requests.get('http://docs.python.org')


html_content = (BeautifulSoup(r.text , features='html.parser').prettify())

with open('~.html' , 'w+') as html:
    for line in (r(html_content).readlines()):

        html.write(html_content)
