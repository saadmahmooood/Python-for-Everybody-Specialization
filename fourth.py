fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.strip()
    if not line.startswith("From "):
        continue
    arr = line.split()
    print(arr[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
