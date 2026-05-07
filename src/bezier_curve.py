import math

def binomial(n,i):
    return math.factorial(n)/(math.factorial(i)*math.factorial(n-i))

def bernstein(i,n,t):
    return binomial(n,i)*pow(t,i)*pow(1.0-t,n-i)

def bezier_curve(ctrl_pts, t):
    bc_x = 0
    bc_y = 0
    bc_z = 0
    for i in range(0, len(ctrl_pts)):
        b = bernstein(i, len(ctrl_pts) - 1, t)
        bc_x = bc_x + b * ctrl_pts[i][0]
        bc_y = bc_y + b * ctrl_pts[i][1]
        bc_z = bc_z + b * ctrl_pts[i][2]
    return (bc_x, bc_y, bc_z)