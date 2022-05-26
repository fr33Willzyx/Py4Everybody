#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse
#and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)

sum = 0
count = 0

for comment in info["comments"]:
    sum += int(comment["count"])
    count += 1

print('Count:', count)
print('Sum:', sum)
