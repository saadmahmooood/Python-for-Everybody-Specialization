import urllib.request
from bs4 import BeautifulSoup

# Function to extract the URL at a given position from the list of anchor tags
def get_next_url(url, position):
    # Open the URL and read the HTML data
    html = urllib.request.urlopen(url).read()
    
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all the anchor tags
    tags = soup('a')
    
    # Extract the href of the anchor tag at the given position
    # Position is 1-based, so we subtract 1 to get the 0-based index
    next_url = tags[position - 1].get('href', None)
    
    # Return the next URL
    return next_url

# Main function to solve the problem
def main():
    # Prompt user for input
    url = input("Enter URL: ")
    count = int(input("Enter count: "))
    position = int(input("Enter position: "))
    
    # Start the process at the given URL
    current_url = url
    print(f"Retrieving: {current_url}")
    
    # Repeat the process for the given count
    for _ in range(count):
        # Get the next URL at the specified position
        next_url = get_next_url(current_url, position)
        
        # Print the URL being retrieved
        print(f"Retrieving: {next_url}")
        
        # Update the current URL
        current_url = next_url
    
    # Extract the last name (the name on the last page)
    last_name = current_url.split('_')[-1].split('.')[0]
    
    # Print the last name found
    print(f"The answer to the assignment is {last_name}")

# Run the main function
if __name__ == "__main__":
    main()
