import math

def binomial(n,i):
    return math.factorial(n)/(math.factorial(i)*math.factorial(n-i))

def bernstein(i,n,t):
    return binomial(n,i)*pow(t,i)*pow(1.0-t,n-i)

def de_casteljau(ctrl_pts, i, j, t):
    if j == 0:
        return ctrl_pts[i]
    else:
        pi   = de_casteljau(ctrl_pts,   i, j-1, t)
        pipu = de_casteljau(ctrl_pts, i+1, j-1, t)
        p_x = (1.0-t)*pi[0] + t*pipu[0]
        p_y = (1.0-t)*pi[1] + t*pipu[1]
        p_z = (1.0-t)*pi[2] + t*pipu[2]
        return (p_x, p_y, p_z)

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

def bezier_curve_subdivision(ctrl_pts, t0):
    ctrl_pts_1 = []
    ctrl_pts_2 = []
    n = len(ctrl_pts)-1
    for i in range(0, len(ctrl_pts)):
        ctrl_pts_1.append(de_casteljau(ctrl_pts, 0, i, t0))
        ctrl_pts_2.append(de_casteljau(ctrl_pts, i, n-i, t0))
    return ctrl_pts_1, ctrl_pts_2