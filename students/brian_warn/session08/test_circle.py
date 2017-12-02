#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# circle.py

'''
tests for Circle class
'''

from circle import Circle
import pytest
from math import pi

def test_init():
	Circle(5)

	assert True


def test_radius():
    c = Circle(5)
    assert c.radius == 5


def test_diameter():
    c = Circle(4)

    assert c.diameter == 8


def test_changed_diameter():
    c = Circle(4)

    assert c.diameter == 8

    c.radius = 5
    assert c.radius == 5
    assert c.diameter == 10


def test_change_diameter():
    c = Circle(4)

    assert c.diameter == 8

    c.diameter = 10
    assert c.radius == 5
    assert c.diameter == 10


def test_area():
    c = Circle(10)
    a = c.area

    assert a == pi * 10**2
    try:
        c.area = 42
    except AttributeError:
        print("Can't set c.area directly.")


def test_set_area():
    c = Circle(10)
    with pytest.raises(AttributeError):
        c.area = 100


def test_delete_diameter():
    c = Circle(10)

    with pytest.raises(AttributeError):
        del c.diameter


def test_add_circle():
    '''
    Step 7

    '''
    c1 = Circle(10)
    c2 = Circle(20)
    c = c1 + c2
    print(c)
    try:
        c2 * 3
    except TypeError:
        print("Can't multiply a Circle object by an integer.")


def test_gt_circle():
    '''
    Step 8
    '''

    c1 = Circle(10)
    c2 = Circle(20)

    try:
        assert c1 > c2
    except AssertionError:
        print("Circle {} is not greater than Circle {}".format(c1, c2))


def test_lt_circle():
    '''
    Step 8
    '''

    c1 = Circle(10)
    c2 = Circle(20)

    try:
        assert c1 < c2
    except AssertionError:
        print("Circle {} is not less than Circle {}".format(c1, c2))


def test_eq_circle():
    '''
    Step 8
    '''
    c1 = Circle(10)
    c2 = Circle(20)
    try:
        assert c1 == c2
    except AssertionError:
        print("{} is not equal to {}".format(c1, c2))

    c1 = Circle(10)
    c2 = Circle(10)
    try:
        assert c1 == c2
    except AssertionError:
        print("{} is not equal to {}".format(c1, c2))



