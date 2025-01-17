# Open the file
filename = "mbox-short.txt"
try:
    file = open(filename, 'r')
except FileNotFoundError:
    print(f"File '{filename}' not found!")
    exit()

# Create a dictionary to store counts by hour
hour_counts = {}

# Process each line in the file
for line in file:
    # Only process lines starting with 'From '
    if line.startswith('From '):
        # Split the line into words
        words = line.split()
        # Extract the time part (5th element)
        time = words[5]
        # Split the time by colon to get the hour
        hour = time.split(':')[0]
        # Increment the count for the hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

file.close()

# Sort the dictionary by hour (key)
sorted_hours = sorted(hour_counts.items())

# Print the counts sorted by hour
for hour, count in sorted_hours:
    print(hour, count)
