#The program will prompt for a URL, read the XML data from that URL
#using urllib and then parse and extract the comment counts from
#the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address)

data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count = 0
sum = 0
for item in results:
    x = int(item.find('count').text)
    count = count + 1
    sum = sum + x
print("Count: ",count)
print("Sum: ",sum)
#counts = tree.findall('.//count')
#print(counts)


#    lat = results[0].find('geometry').find('location').find('lat').text
#    lng = results[0].find('geometry').find('location').find('lng').text
#    location = results[0].find('formatted_address').text
