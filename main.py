from plt.plot_bezier_curve import *
from plt.plot_bspline_curve import *
from src.bspline_curve import *

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    # Test case NURBS Book page 84
    knots = [0, 0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1, 1]
    ctrl_pts = [(-1, 0, 0), (1, 0, 1), (1, 2, 2), (4, 2, 3), (4.5, 0, 4), (2.5, -1, 5), (1, -0.6, 6)]

    plot_bspline(knots, ctrl_pts)
    plot_all_bsplines_basis(knots, 3)

    knots = [0, 0, 0, 0.2, 0.4, 0.6, 0.8, 0.8, 1, 1, 1]
    plot_all_bsplines_basis(knots, 2)

    # Test Bezier Curve
    ctrl_pts = [(0,0,0), (0.4,-0.1,0.4), (0.6,1.1,0.4), (1,1,0)]
    plot_bezier_curve(ctrl_pts, 100)

    #
    print("BEZIER CURVE SUBDIVISER")
    ctrl_pts_1, ctrl_pts_2 = bezier_curve_subdivision(ctrl_pts, 0.5)

    sample = 100
    t = np.linspace(0, 1, sample)
    p0_x = []
    p0_y = []
    p0_z = []
    p1_x = []
    p1_y = []
    p1_z = []
    p2_x = []
    p2_y = []
    p2_z = []
    for i in range(0, sample):
        p0 = bezier_curve(ctrl_pts, t[i])
        p0_x.append(p0[0])
        p0_y.append(p0[1])
        p0_z.append(p0[2])
        p1 = bezier_curve(ctrl_pts_1, t[i])
        p1_x.append(p1[0])
        p1_y.append(p1[1])
        p1_z.append(p1[2])
        p2 = bezier_curve(ctrl_pts_2, t[i])
        p2_x.append(p2[0])
        p2_y.append(p2[1])
        p2_z.append(p2[2])

    fig = plt.figure().add_subplot(projection='3d')
    fig.plot(p0_x, p0_y, p0_z, color='black', linewidth=2, label="Bezier Curve")
    fig.plot(p1_x, p1_y, p1_z, linestyle='dashed', linewidth=2, label="Bezier Curve - Part 1")
    fig.plot(p2_x, p2_y, p2_z, linestyle='dashed', linewidth=2, label="Bezier Curve - Part 2")
    #fig.plot(ctrl_pts_x, ctrl_pts_y, ctrl_pts_z, marker='8', color='grey', linewidth=1, linestyle='dashed', label='Control Points')
    fig.set_xlabel('X')
    fig.set_ylabel('Y')
    fig.set_zlabel('Z')
    fig.grid()
    fig.legend()
    plt.show()