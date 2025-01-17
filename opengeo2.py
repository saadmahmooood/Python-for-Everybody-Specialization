import urllib.request, urllib.parse
import json, ssl

# Base URL for the OpenGeo API
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Prompt for a location
    address = input('Enter location: ')
    if len(address) < 1:
        break

    # Build the URL with encoded parameters
    parms = {'q': address.strip()}
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    # Retrieve the data from the URL
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        # Parse the JSON data
        js = json.loads(data)
    except json.JSONDecodeError:
        js = None

    if not js or 'plus_code' not in js:
        print('==== Download error ===')
        print(data)
        break

    # Extract and print the plus_code
    plus_code = js['plus_code']
    print('Plus code', plus_code)
    break
