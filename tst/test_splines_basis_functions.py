from src.bspline_curve import *

def test_bspline_basis_functions_2_1():
    # Test Case NURBS BOOK, p.52, Ex2.1.
    # B-Spline of degree p=2
    # U = {0, 0, 0, 1, 1, 1}

    knots_test = [0, 0, 0, 1, 1, 1]
    assert(bspline_basis_function(knots_test, 0, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 0, 0, 10) == 0)

    assert(bspline_basis_function(knots_test, 1, 0, 0.5) == 0)
    assert(bspline_basis_function(knots_test, 1, 0, 1.2) == 0)

    assert(bspline_basis_function(knots_test, 2, 0, 0) == 1)
    assert(bspline_basis_function(knots_test, 2, 0, -2) == 0)

    assert(bspline_basis_function(knots_test, 0, 1, 0) == 0)
    assert(bspline_basis_function(knots_test, 0, 1, 1.6) == 0)

    assert(bspline_basis_function(knots_test, 1, 1, -0.1) == 0)
    assert(bspline_basis_function(knots_test, 1, 1, 0) == 1) # Supposed to be 1-t
    assert(bspline_basis_function(knots_test, 1, 1, 0.25) == 0.75)
    assert(bspline_basis_function(knots_test, 1, 1, 0.5) == 0.5)
    assert(bspline_basis_function(knots_test, 1, 1, 1) == 0)
    assert(bspline_basis_function(knots_test, 1, 1, 1.1) == 0)

    assert(bspline_basis_function(knots_test, 2, 1, -0.1) == 0)
    assert(bspline_basis_function(knots_test, 2, 1, 0) == 0) # Supposed to be t
    assert(bspline_basis_function(knots_test, 2, 1, 0.25) == 0.25)
    assert(bspline_basis_function(knots_test, 2, 1, 0.5) == 0.5)
    assert(bspline_basis_function(knots_test, 2, 1, 1) == 0)
    assert(bspline_basis_function(knots_test, 2, 1, 1.1) == 0)

    assert(bspline_basis_function(knots_test, 0, 2, -0.1) == 0)
    assert(bspline_basis_function(knots_test, 0, 2, 0) == 1) # Supposed to be (1-t)^2
    assert(bspline_basis_function(knots_test, 0, 2, 0.25) == 0.5625)
    assert(bspline_basis_function(knots_test, 0, 2, 0.5) == 0.25)
    assert(bspline_basis_function(knots_test, 0, 2, 1) == 0)
    assert(bspline_basis_function(knots_test, 0, 2, 1.1) == 0)

    assert(bspline_basis_function(knots_test, 1, 2, -0.1) == 0)
    assert(bspline_basis_function(knots_test, 1, 2, 0) == 0) # Supposed to be 2t(1-t)
    assert(bspline_basis_function(knots_test, 1, 2, 0.25) == 0.375)
    assert(bspline_basis_function(knots_test, 1, 2, 0.5) == 0.5)
    assert(bspline_basis_function(knots_test, 1, 2, 1) == 0)
    assert(bspline_basis_function(knots_test, 1, 2, 1.1) == 0)

def test_bspline_basis_functions_2_2():
    # Test Case NURBS BOOK, p.52, Ex2.2.
    # B-Spline of degree p=2
    # U = {0, 0, 0, 0.2, 0.4, 0.6, 0.8, 0.8, 1, 1, 1}

    knots_test = [0, 0, 0, 0.2, 0.4, 0.6, 0.8, 0.8, 1, 1, 1]

    assert(bspline_basis_function(knots_test, 0, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 0, 0, 0.5) == 0)
    assert(bspline_basis_function(knots_test, 0, 0, 1) == 0)

    assert(bspline_basis_function(knots_test, 1, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 1, 0, 0.5) == 0)
    assert(bspline_basis_function(knots_test, 1, 0, 1) == 0)

    assert(bspline_basis_function(knots_test, 2, 0, 0) == 1)
    assert(bspline_basis_function(knots_test, 2, 0, 0.1) == 1)
    assert(bspline_basis_function(knots_test, 2, 0, 0.2) == 0)

    assert(bspline_basis_function(knots_test, 3, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 3, 0, 0.2) == 1)
    assert(bspline_basis_function(knots_test, 3, 0, 0.4) == 0)

    assert(bspline_basis_function(knots_test, 4, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 4, 0, 0.4) == 1)
    assert(bspline_basis_function(knots_test, 4, 0, 0.6) == 0)

    assert(bspline_basis_function(knots_test, 5, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 5, 0, 0.6) == 1)
    assert(bspline_basis_function(knots_test, 5, 0, 0.8) == 0)

    assert(bspline_basis_function(knots_test, 6, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 6, 0, 0.5) == 0)
    assert(bspline_basis_function(knots_test, 6, 0, 0.7) == 0)
    assert(bspline_basis_function(knots_test, 6, 0, 1) == 0)

    assert(bspline_basis_function(knots_test, 7, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 7, 0, 0.8) == 1)
    assert(bspline_basis_function(knots_test, 7, 0, 1) == 0)

    assert(bspline_basis_function(knots_test, 8, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 8, 0, 0.5) == 0)
    assert(bspline_basis_function(knots_test, 8, 0, 1) == 0)

    assert(bspline_basis_function(knots_test, 9, 0, 0) == 0)
    assert(bspline_basis_function(knots_test, 9, 0, 0.5) == 0)
    assert(bspline_basis_function(knots_test, 9, 0, 1) == 0)


    assert(bspline_basis_function(knots_test, 0, 1, 0) == 0)
    assert(bspline_basis_function(knots_test, 0, 1, 0.25) == 0)
    assert(bspline_basis_function(knots_test, 0, 1, 0.5) == 0)
    assert(bspline_basis_function(knots_test, 0, 1, 1) == 0)

    assert(bspline_basis_function(knots_test, 1, 1, 0) == 1)  # 1-5u for 0 <= u < 0.2
    assert(bspline_basis_function(knots_test, 1, 1, 0.1) == 0.5)
    assert(abs(bspline_basis_function(knots_test, 1, 1, 0.15) - 0.25) < 1e-9)
    assert(bspline_basis_function(knots_test, 1, 1, 0.2) == 0)
    assert(bspline_basis_function(knots_test, 1, 1, 1) == 0)

    assert(bspline_basis_function(knots_test, 2, 1, 0) == 0)      # 5u for 0 <= u < 0.2
    assert(bspline_basis_function(knots_test, 2, 1, 0.1) == 0.5)    # 2 - 5u for 0.2 <= u < 0.4
    assert(abs(bspline_basis_function(knots_test, 2, 1, 0.2) - 1.0) < 1e-9)
    assert(bspline_basis_function(knots_test, 2, 1, 0.4) == 0)
    assert(bspline_basis_function(knots_test, 2, 1, 1) == 0)