def bspline_basis_function(knots, i, n, t):
    """
    Cox De Boor relation.

    :param knots:
    :param i:
    :param n:
    :param t:
    :return:
    """
    if n == 0:
        if knots[i] <= t < knots[i + 1]:
            return 1
        else:
            return 0
    if knots[i] > t or t >= knots[i+n+1]:
        return 0
    s = 0
    if knots[i+n] != knots[i]:
        a = (t-knots[i])/(knots[i+n]-knots[i])
        s += a * bspline_basis_function(knots, i, n - 1, t)
    if knots[i+n+1] != knots[i+1]:
        b = (knots[i+n+1]-t)/(knots[i+n+1]-knots[i+1])
        s += b * bspline_basis_function(knots, i + 1, n - 1, t)
    return s

def bspline(knots, ctrl_pts, t):
    """
    n is the degree of the B Spline.
    :param knots: vector of m+1 knots, numbered from 0 to m
    :param ctrl_pts: vector of m-n control points
    :param t:
    :return:
    """
    m = len(knots)-1
    n = m-len(ctrl_pts) # n is the degree
    # compute the bspline position
    x = 0
    y = 0
    z = 0
    for i in range(0, len(ctrl_pts)):
        bs = bspline_basis_function(knots, i, n, t)
        x += ctrl_pts[i][0] * bs
        y += ctrl_pts[i][1] * bs
        z += ctrl_pts[i][2] * bs
    return (x, y, z)

