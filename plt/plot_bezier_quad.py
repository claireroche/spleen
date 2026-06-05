import numpy as np
import matplotlib.pyplot as plt

from src.bezier_quad import *

def plot_bezier_quad(ctrl_pts, u_sample, v_sample):
    u = np.linspace(0, 1, u_sample)
    v = np.linspace(0, 1, v_sample)
    point_x = []
    point_y = []
    point_z = []
    for i in range(0,u_sample):
        for j in range(0, v_sample):
            point = bezier_quad(ctrl_pts, u[i], v[j])
            point_x.append(point[0])
            point_y.append(point[1])
            point_z.append(point[2])

    ctrl_pts_x = []
    ctrl_pts_y = []
    ctrl_pts_z = []
    for i in range(0,len(ctrl_pts[0])):
        for j in range(0, len(ctrl_pts)):
            ctrl_pt = ctrl_pts[i][j]
            ctrl_pts_x.append(ctrl_pt[0])
            ctrl_pts_y.append(ctrl_pt[1])
            ctrl_pts_z.append(ctrl_pt[2])

    fig = plt.figure().add_subplot(projection='3d')
    fig.plot(point_x, point_y, point_z, marker='.', color='black', linestyle='none', label='Bezier Quad')
    fig.plot(ctrl_pts_x, ctrl_pts_y, ctrl_pts_z, marker='8', color='grey', linestyle='none', label='Control Points')
    fig.set_xlabel('X')
    fig.set_ylabel('Y')
    fig.set_zlabel('Z')
    fig.set_xlim(0, 1.0)
    fig.set_ylim(0, 1.0)
    fig.set_zlim(0, 0.5)
    fig.grid()
    fig.legend()
    plt.show()


def plot_multiple_bezier_quad(list_ctrl_pts, u_sample, v_sample):
    u = np.linspace(0, 1, u_sample)
    v = np.linspace(0, 1, v_sample)
    pts_x = []
    pts_y = []
    pts_z = []
    for ctrl_pts in list_ctrl_pts:
        point_x = []
        point_y = []
        point_z = []
        for i in range(0,u_sample):
            for j in range(0, v_sample):
                point = bezier_quad(ctrl_pts, u[i], v[j])
                point_x.append(point[0])
                point_y.append(point[1])
                point_z.append(point[2])
        pts_x.append(point_x)
        pts_y.append(point_y)
        pts_z.append(point_z)

    ctrl_pts_x = []
    ctrl_pts_y = []
    ctrl_pts_z = []
    for ctrl_pts in list_ctrl_pts:
        for i in range(0,len(ctrl_pts[0])):
            for j in range(0, len(ctrl_pts)):
                ctrl_pt = ctrl_pts[i][j]
                ctrl_pts_x.append(ctrl_pt[0])
                ctrl_pts_y.append(ctrl_pt[1])
                ctrl_pts_z.append(ctrl_pt[2])

    fig = plt.figure().add_subplot(projection='3d')
    for i in range(0, len(pts_x)):
        fig.plot(pts_x[i], pts_y[i], pts_z[i], marker='.', linestyle='none')
    fig.plot(ctrl_pts_x, ctrl_pts_y, ctrl_pts_z, marker='8', color='grey', linestyle='none', label='Control Points')
    fig.set_xlabel('X')
    fig.set_ylabel('Y')
    fig.set_zlabel('Z')
    fig.set_xlim(0, 1.0)
    fig.set_ylim(0, 1.0)
    fig.set_zlim(0, 0.5)
    fig.grid()
    fig.legend()
    plt.show()