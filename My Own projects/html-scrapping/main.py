from bs4 import BeautifulSoup

with open('E:\GIthub repos\Learn-Python\My Own projects\html-scrapping\\1.html' , 'r') as f:
    doc = BeautifulSoup(f , 'html.parser')

print (doc.prettify())

# tag = doc.a

# print(tag)