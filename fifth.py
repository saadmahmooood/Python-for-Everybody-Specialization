handle = open("mbox-short.txt")
maxCount = None
maxWord = None
email_list = dict()

for line in handle:
    line = line.strip()
    # Skip lines that do not start with 'From '
    if not line.startswith("From "):
        continue
    
    arr = line.split()
    # Extract the email address (second word in the line)
    email = arr[1]
    
    # Increment the count for the email in the dictionary
    email_list[email] = email_list.get(email, 0) + 1

# Find the most prolific sender
for email, count in email_list.items():
    if maxCount is None or count > maxCount:
        maxCount = count
        maxWord = email

print(f"The most prolific sender is: {maxWord} with {maxCount} messages.")
