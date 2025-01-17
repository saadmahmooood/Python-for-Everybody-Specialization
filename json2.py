import urllib.request
import json

# Prompt for a URL
url = input("Enter location: ")
print("Retrieving", url)

# Retrieve the JSON data from the URL
response = urllib.request.urlopen(url)
data = response.read()
print("Retrieved", len(data), "characters")

# Parse the JSON data
info = json.loads(data)

# Extract the comment counts and compute the sum
comments = info.get('comments', [])
total_count = sum(item['count'] for item in comments)

# Print the results
print("Count:", len(comments))
print("Sum:", total_count)
