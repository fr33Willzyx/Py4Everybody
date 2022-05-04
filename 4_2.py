h = input("Enter Hours:")
r = input("Enter Rate:")

def computepay(h, r):
    if float(h) > 40 :
        return (float(r) * 40) + (1.5 * float(r) * (float(h) - 40))
    else:
        return h * r
   
p = computepay(h, r)
print("Pay", p)
