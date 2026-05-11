import numpy as np
import matplotlib.pyplot as plt

from src.bezier_curve import *

def plot_bezier_curve(ctrl_pts, sample):
    t = np.linspace(0, 1, sample)
    point_x = []
    point_y = []
    point_z = []
    for i in range(0,sample):
        point = bezier_curve(ctrl_pts, t[i])
        point_x.append(point[0])
        point_y.append(point[1])
        point_z.append(point[2])

    ctrl_pts_x = []
    ctrl_pts_y = []
    ctrl_pts_z = []
    for ctrl_pt in ctrl_pts:
        ctrl_pts_x.append(ctrl_pt[0])
        ctrl_pts_y.append(ctrl_pt[1])
        ctrl_pts_z.append(ctrl_pt[2])

    fig = plt.figure().add_subplot(projection='3d')
    fig.plot(point_x, point_y, point_z, color='black', linewidth=2, label="Bezier Curve")
    fig.plot(ctrl_pts_x, ctrl_pts_y, ctrl_pts_z, marker='8', color='grey', linewidth=1, linestyle='dashed', label='Control Points')
    fig.set_xlabel('X')
    fig.set_ylabel('Y')
    fig.set_zlabel('Z')
    fig.grid()
    fig.legend()
    plt.show()