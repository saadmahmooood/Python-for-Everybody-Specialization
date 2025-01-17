import re

# File name (replace with your actual file name if needed)
file_name = "actual.txt"

# Open the file
try:
    with open(file_name, 'r') as file:
        data = file.read()
        
    # Find all numbers using regular expressions
    numbers = re.findall('[0-9]+', data)
    
    # Convert strings to integers using a loop
    integers = []
    for number in numbers:
        integers.append(int(number))
    
    # Calculate the sum of the integers
    total_sum = 0
    for num in integers:
        total_sum += num
    
    # Print the result
    print(total_sum)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Please make sure the file exists in the same directory.")
