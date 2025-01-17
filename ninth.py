import urllib.request
from bs4 import BeautifulSoup

# Prompt user for the URL input
url = input("Enter - ")

# Open the URL and read the HTML data
html = urllib.request.urlopen(url).read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <span> tags that contain the numbers
tags = soup('span')

# Initialize a variable to store the sum of numbers
sum_of_numbers = 0
count = 0

# Loop through each <span> tag
for tag in tags:
    # Extract the text content and try converting it to an integer
    try:
        num = int(tag.contents[0])
        sum_of_numbers += num
        count += 1
    except ValueError:
        # If the content is not a number, skip it
        continue

# Print the count and sum of numbers
print(f"Count {count}")
print(f"Sum {sum_of_numbers}")
