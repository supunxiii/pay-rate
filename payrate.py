def computepay(h,r):
    h = float(hrs)
    r = float(rate_per_hour)
    if h > 40:
        hrs_mre = h - 40
        p = 40 * r + 1.5 * r * hrs_mre
    else:
        p = h * r
    return p
   
hrs = input("Enter Hours: ")
rate_per_hour = input("Enter Rate Per Hour: ")
p = computepay(hrs,rate_per_hour)
print("Pay", p)
