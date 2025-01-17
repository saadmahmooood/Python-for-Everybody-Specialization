total = 0
count = 0
avg = None

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        number = float(number)
        count += 1
        total += number
    except:
        print("Invalid Input")

if count > 0:
    avg = total / count
    print(total, count, avg)
else:
    print("No numbers were entered.")
