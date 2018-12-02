# Find out if a number is odd or even

def evenodd(n):
    if n % 2 == 0:
        print str(n) + " is even"
    else:
        print str(n) + " is odd"

m = int(raw_input("n = "))

evenodd(m)
