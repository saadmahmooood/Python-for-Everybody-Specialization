import urllib.request
import xml.etree.ElementTree as ET

# Prompt the user for a URL
url = input('Enter location: ')
if len(url) < 1: 
    url = 'http://py4e-data.dr-chuck.net/comments_2154520.xml'

print('Retrieving', url)

# Open the URL and read the data
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Parse the XML data
tree = ET.fromstring(data)

# Find all 'count' elements in the XML
counts = tree.findall('.//count')

# Collect and sum the numbers
total = 0
for result in counts:
    # Convert text to integer and add to total
    num = int(result.text)
    total += num

print('Count:', len(counts))
print('Sum:', total)
