from price_tools import highest
def test_highest_basic():
    assert highest([10,30,50,98,76,99,89,10]) == 99
def test_highest_one_item():
    assert highest([1])==1
def test_highest_tie():
    assert highest([23,23]) == 23