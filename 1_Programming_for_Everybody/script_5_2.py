largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest == None or largest < num:
            largest = num
        if smallest == None or smallest > num:
            smallest = num
    except:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)