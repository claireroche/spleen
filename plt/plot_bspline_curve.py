from src.bspline_curve import *

import matplotlib.pyplot as plt
import numpy as np

def plot_bsplines_basis(knots, n):
    for i in range(0,len(knots)-1-n):
        t_vals = np.linspace(knots[i], knots[i+n+1], 201)[1:-1]
        y = []
        for t in t_vals:
            y.append(bspline_basis_function(knots, i, n, t))
        plt.plot(t_vals, y, label="N_%.2d,%.2d" %(i, n))

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid()
    plt.show()


def plot_all_bsplines_basis(knots, n):
    fig, ax = plt.subplots(n+1)
    for p in range(0,n+1):
        for i in range(0,len(knots)-1-p):
            t_vals = np.linspace(knots[i], knots[i+p+1], 201)[1:-1]
            y = []
            for t in t_vals:
                y.append(bspline_basis_function(knots, i, p, t))
            ax[p].plot(t_vals, y, label="N_%.d,%.d" %(i, p))
            ax[p].set_xlim(-0.05,1.2)
            ax[p].legend(loc='right')
    for axe in ax:
        axe.grid()
    #plt.grid()
    plt.show()


def plot_bspline(knots, ctrl_pts):
    fig = plt.figure().add_subplot(projection='3d')
    for j in range(0, len(knots)-1):
        t_vals = np.linspace(knots[j], knots[j+1], 101)[:-1]
        point_x = []
        point_y = []
        point_z = []
        for i in range(0,100):
            point = bspline_curve(knots, ctrl_pts, t_vals[i])
            point_x.append(point[0])
            point_y.append(point[1])
            point_z.append(point[2])
        if j%2 == 0:
            fig.plot(point_x, point_y, point_z, color='black', linewidth=2)
        else:
            fig.plot(point_x, point_y, point_z, color='black', linestyle='dashed', linewidth=2)

    ctrl_pts_x = []
    ctrl_pts_y = []
    ctrl_pts_z = []
    for ctrl_pt in ctrl_pts:
        ctrl_pts_x.append(ctrl_pt[0])
        ctrl_pts_y.append(ctrl_pt[1])
        ctrl_pts_z.append(ctrl_pt[2])

    points_knots_x = []
    points_knots_y = []
    points_knots_z = []
    for knot in knots:
        if knot > 0 and knot < 1:
            point = bspline_curve(knots, ctrl_pts, knot)
            points_knots_x.append(point[0])
            points_knots_y.append(point[1])
            points_knots_z.append(point[2])

    fig.plot(ctrl_pts_x, ctrl_pts_y, ctrl_pts_z, marker='8', color='grey', linewidth=1, linestyle='dashed', label='Control Points')
    fig.plot(points_knots_x, points_knots_y, points_knots_z, marker='o', color='black', linestyle='none', label='Knots')
    fig.set_xlabel('X')
    fig.set_ylabel('Y')
    fig.set_zlabel('Z')
    #fig.set_xlim(-1, 4)
    #fig.set_ylim(-1, 4)
    #fig.set_zlim(-1, 4)
    fig.legend()
    fig.grid()
    plt.show()