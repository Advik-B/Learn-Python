from googlesearch import search

import os
import subprocess
# to search
while True:
    print('What is the query? (0 to quit)')

    query = input('$ ')
    if query == 0:
        break
    print()

    print('How many number of results do you want? (the more the better!) 0 to quit')
    
    number_query = int(input('$ '))
    if number_query == 0:
        print()
        break

    # query = "Minecraft"
    if query == None or query == '':
        query = '%20'
    file = open(f'{query}.txt','w+')
    print()
    print('fetching results please wait...')
    print()
    
    for j in search(query, tld="co.in", num=number_query, stop=number_query, pause=15):
        print(j)
        file.write(f"{j}\n")
    print()

    if os.path.isfile('./.google-cookie'):
        subprocess.call('powershell rm .google-cookie')
    file.close()

input('press enter to quit')