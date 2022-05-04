hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h <= 40 :
    Pay = h * r
else :
    Pay = (1.5 * r * (h - 40)) + 40 * r
print(Pay)
