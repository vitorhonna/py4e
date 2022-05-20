def computepay(h, r):
    if h <= 40:
        p = h*r
    else:
        p = (40*r) + ((h-40)*r*1.5)
    return p

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

print("Pay", computepay(hrs, rate))
