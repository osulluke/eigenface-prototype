import time
import requests

file = open("unique-links.txt",'r')
links = []

# Create a list of sites to scrape
for l in file:
    links.append(l)

# Scrape each link
for link in links:
    time.sleep(4.5)
    file_name = 'collected-img/' + link.split('/')[-1].replace('\n','.jpg')
    image = requests.get(link.replace('\n','')).content
    with open(file_name, 'wb') as handler:
        handler.write(image)