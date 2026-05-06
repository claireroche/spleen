import math

def binomial(n,i):
    return math.factorial(n)/(math.factorial(i)*math.factorial(n-i))

def bernstein(i,n,t):
    return binomial(n,i)*pow(t,i)*pow(1.0-t,n-i)

def bezier(pts, t):
    sum = 0
    for i in range(0,len(pts)):
        sum = sum + bernstein(i,len(pts)-1,t)*pts[i]
    return sum

assert(binomial(10,10)==1)
assert(binomial(10,5)==252)

#print(bezier([0,0.3,0.7,1], 0.5))

