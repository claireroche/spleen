import math

def binomial(n,i):
    return math.factorial(n)/(math.factorial(i)*math.factorial(n-i))

def bernstein(i,n,t):
    return binomial(n,i)*pow(t,i)*pow(1.0-t,n-i)

def bezier_curve(ctrl_pts, t):
    bc = 0
    for i in range(0, len(ctrl_pts)):
        bc = bc + bernstein(i, len(ctrl_pts) - 1, t) * ctrl_pts[i]
    return bc