from price_tools import highest, daily_returns, average_price, moving_average
from ex3 import count_currencies,count_up_days,biggest_drop
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
        
def test_count_up_days_zero():
    assert count_up_days([12,12,12,12,12])==0
    
def test_count_up_days_negative_prices():
    with pytest.raises(ValueError):
        count_up_days([12,14,10,6,9,14,10,0,0,-4,0])
    
def test_count_up_days_empty():
    with pytest.raises(ValueError):
        count_up_days([]) 
        
def test_count_up_days_basic():
    assert count_up_days([1,2,3,4,9,8,7,6,5,4,10])==5 
    

def test_count_currencies_small_letters():
    assert count_currencies(["usd", "USD", "usD"]) == {"USD": 3}
    
def test_count_currencies_basic():
    assert count_currencies(["LBP","USD","EUR","AED","AED","USD","USD","AED"]) == {"LBP": 1,"USD": 3,"EUR": 1,"AED": 3}
    
def test_count_currencies_empty():
    assert count_currencies([])=={}

def test_count_currencies_one_item():
    assert count_currencies(["LBP"])=={"LBP": 1}
    
def test_biggest_drop_basic():
    assert biggest_drop([130,120,150,180,110,10,200,300,200,200]) == 100
    
def test_biggest_drop_stable():
    assert biggest_drop([10,10,10])==0
    
def test_biggest_drop_no_drop():
    assert biggest_drop([10,20,30])==0
    
def test_moving_average_empty_list():
    assert moving_average([],1)==[]
    
def test_moving_average_window_too_large():
    assert moving_average([2,3,4],5)==[]
    
def test_moving_average_basic():
    assert moving_average([2,3,2,4,5,6,7],3)==[2.33,3.0,3.67,5.0,6.0]
    
def test_moving_average_zero_n():
    with pytest.raises(ValueError):
        moving_average([1,2,3,4], 0)
    
def test_moving_average_negative_n():
    with pytest.raises(ValueError):
        moving_average([1,2,3,4],-3)
