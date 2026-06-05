import math
import src.bezier_curve as spleen_bc

def bezier_quad(ctrl_pts, u, v):
    bc_x = 0
    bc_y = 0
    bc_z = 0
    for i in range(0, len(ctrl_pts[0])):
        bi = spleen_bc.bernstein(i, len(ctrl_pts[0]) - 1, u)
        for j in range(0, len(ctrl_pts)):
            bj = spleen_bc.bernstein(j, len(ctrl_pts) - 1, v)
            bc_x = bc_x + bi * bj * ctrl_pts[i][j][0]
            bc_y = bc_y + bi * bj * ctrl_pts[i][j][1]
            bc_z = bc_z + bi * bj * ctrl_pts[i][j][2]
    return (bc_x, bc_y, bc_z)

def bezier_quad_subdivision(ctrl_pts, t0):
    ctrl_pts_1 = []
    ctrl_pts_2 = []
    n = len(ctrl_pts)-1
    m = len(ctrl_pts[0])-1
    for i in range(0, len(ctrl_pts)):
        ctrl_pts_1.append([])
        ctrl_pts_2.append([])
        for j in range(0, len(ctrl_pts[0])):
            ctrl_pts_1[i].append(spleen_bc.de_casteljau(ctrl_pts[i], 0,   j, t0))
            ctrl_pts_2[i].append(spleen_bc.de_casteljau(ctrl_pts[i], j, m-j, t0))
    return ctrl_pts_1, ctrl_pts_2