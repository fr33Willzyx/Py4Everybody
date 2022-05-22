#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
numlist = list()
tags = soup('span')
for tag in tags:
    # Convert tags to strings
    y = str(tag)
    #Pull the number from each string and add them to our list
    nums = re.findall('[0-9]+', y)
    for i in nums:
        i = int(i)
        numlist.append(i)
print(sum(numlist))
