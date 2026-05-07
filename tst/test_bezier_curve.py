import src.bezier_curve as spleen_bezier_curve

def test_binomial():

    assert(spleen_bezier_curve.binomial(1, 0) == 1)
    assert(spleen_bezier_curve.binomial(1, 1) == 1)

    assert(spleen_bezier_curve.binomial(2, 0) == 1)
    assert(spleen_bezier_curve.binomial(2, 1) == 2)
    assert(spleen_bezier_curve.binomial(2, 2) == 1)

    assert(spleen_bezier_curve.binomial(3, 0) == 1)
    assert(spleen_bezier_curve.binomial(3, 1) == 3)
    assert(spleen_bezier_curve.binomial(3, 2) == 3)
    assert(spleen_bezier_curve.binomial(3, 3) == 1)

    assert(spleen_bezier_curve.binomial(4, 0) == 1)
    assert(spleen_bezier_curve.binomial(4, 1) == 4)
    assert(spleen_bezier_curve.binomial(4, 2) == 6)
    assert(spleen_bezier_curve.binomial(4, 3) == 4)
    assert(spleen_bezier_curve.binomial(4, 4) == 1)

    assert(spleen_bezier_curve.binomial(5, 0) == 1)
    assert(spleen_bezier_curve.binomial(5, 1) == 5)
    assert(spleen_bezier_curve.binomial(5, 2) == 10)
    assert(spleen_bezier_curve.binomial(5, 3) == 10)
    assert(spleen_bezier_curve.binomial(5, 4) == 5)
    assert(spleen_bezier_curve.binomial(5, 5) == 1)

    assert(spleen_bezier_curve.binomial(6, 0) == 1)
    assert(spleen_bezier_curve.binomial(6, 1) == 6)
    assert(spleen_bezier_curve.binomial(6, 2) == 15)
    assert(spleen_bezier_curve.binomial(6, 3) == 20)
    assert(spleen_bezier_curve.binomial(6, 4) == 15)
    assert(spleen_bezier_curve.binomial(6, 5) == 6)
    assert(spleen_bezier_curve.binomial(6, 6) == 1)

    assert(spleen_bezier_curve.binomial(7, 0) == 1)
    assert(spleen_bezier_curve.binomial(7, 1) == 7)
    assert(spleen_bezier_curve.binomial(7, 2) == 21)
    assert(spleen_bezier_curve.binomial(7, 3) == 35)
    assert(spleen_bezier_curve.binomial(7, 4) == 35)
    assert(spleen_bezier_curve.binomial(7, 5) == 21)
    assert(spleen_bezier_curve.binomial(7, 6) == 7)
    assert(spleen_bezier_curve.binomial(7, 7) == 1)

    assert(spleen_bezier_curve.binomial(8, 0) == 1)
    assert(spleen_bezier_curve.binomial(8, 1) == 8)
    assert(spleen_bezier_curve.binomial(8, 2) == 28)
    assert(spleen_bezier_curve.binomial(8, 3) == 56)
    assert(spleen_bezier_curve.binomial(8, 4) == 70)
    assert(spleen_bezier_curve.binomial(8, 5) == 56)
    assert(spleen_bezier_curve.binomial(8, 6) == 28)
    assert(spleen_bezier_curve.binomial(8, 7) == 8)
    assert(spleen_bezier_curve.binomial(8, 8) == 1)

    assert(spleen_bezier_curve.binomial(10, 10) == 1)
    assert(spleen_bezier_curve.binomial(10, 5) == 252)


def test_bernstein():

    # for n=0, B_0^0(t) = 1
    assert(spleen_bezier_curve.bernstein(0, 0,    0) == 1)
    assert(spleen_bezier_curve.bernstein(0, 0, 0.25) == 1)
    assert(spleen_bezier_curve.bernstein(0, 0, 0.75) == 1)
    assert(spleen_bezier_curve.bernstein(0, 0,    1) == 1)

    # for n=1, B_0^1(t) = 1-t
    assert(spleen_bezier_curve.bernstein(0, 1,    0) == 1)
    assert(spleen_bezier_curve.bernstein(0, 1, 0.25) == 0.75)
    assert(spleen_bezier_curve.bernstein(0, 1, 0.75) == 0.25)
    assert(spleen_bezier_curve.bernstein(0, 1,    1) == 0)

    # for n=1, B_1^1(t) = t
    assert(spleen_bezier_curve.bernstein(1, 1,    0) == 0)
    assert(spleen_bezier_curve.bernstein(1, 1, 0.25) == 0.25)
    assert(spleen_bezier_curve.bernstein(1, 1, 0.75) == 0.75)
    assert(spleen_bezier_curve.bernstein(1, 1,    1) == 1)