
from sumup import sumup

def test_sum():
    assert sumup([1, 2, 3, 4, 5]) == 15
    assert sumup([0, 1, 2]) >= 2

def test_sum2():
    assert sumup([0, 1, 2]) == 3

def test_sum3():
    assert sumup([1, 3, 4]) != 12

def test_it():
    assert sumup([1, 3, 4]) == 8

# lancer test avec pytest