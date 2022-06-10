# Have a Great Day!!!  :)
# Azothoth
def mydef(h,r):
    if h > 40:
        return (40*r)+(h-40)*(r*1.5)
    else:
        return h*r


hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))


hrs = float(hrs)
rate = float(rate)

p = mydef(hrs, rate)
print (p)