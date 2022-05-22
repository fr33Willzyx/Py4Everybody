#The program will use urllib to read the HTML from the data files below, extract the href=
#vaues from the anchor tags, scan for a tag that is in a particular position relative to the
#first name in the list, follow that link and repeat the process a number of times and report the last name you find
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter Count: '))
position = int(input('Enter Position: '))
tags_lst = list()

# Retrieve all of the anchor tags
for x in range(0, count):
        tags = soup('a')
        tag = tags[position - 1]
        needed_tag = tag.get('href', None)
        tags_lst.append(needed_tag)
        url = str(needed_tag)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        print(tag.get('href', None))
