# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        star = line.find(' ')
        line = line[star:]
        total = total + float(line) 
        count = count + 1

avg = total/count
print("Average spam confidence:",avg)

