import math
p = 29
ints = [14, 6, 11]
gcdArray = [i for i in range(1,p) if math.gcd(p,i) == 1]

for i in (gcdArray):
    for ii in ints:
        for iii in range(1, 50):
            if ((pow(i,2)) - ii == iii*p):
                print(i)

