import os
import time
import requests
from googlesearch import search
p = print
P = p

for answer in search('Python Download' , stop=10 , safe=True):
    p(answer)