from price_tools import highest, daily_returns, average_price
import pytest


def test_highest_basic():
    assert highest([10,30,50,98,76,99,89,10]) == 99

def test_highest_one_item():
    assert highest([1])==1

def test_highest_tie():
    assert highest([23,23]) == 23

def test_daily_return_one_item():
    assert daily_returns([12]) == []

def test_daily_returns_basic():
    assert daily_returns([100,200]) == [100]

def test_daily_returns_flat():
    assert daily_returns([130,130,130]) == [0,0]

def test_daily_returns_with_zeroes():
    with pytest.raises(ValueError):
        daily_returns([0,0,0,0])

def test_daily_returns_negative_price():
    with pytest.raises(ValueError):
        daily_returns([100, -5, 90])

def test_average_price_basic():
    assert average_price([1,2,3,4,5]) == 3

def test_average_price_empty_list():
    with pytest.raises(ValueError):
        average_price([])

def test_average_price_floats():
    assert average_price([1.9999,3.55555])==2.78

def test_average_price_zero():
    with pytest.raises(ValueError):
        average_price([6,8,3,9,0])