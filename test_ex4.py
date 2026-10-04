from ex4 import is_palindrome_corrected, count_words_corrected,second_largest_corrected
import pytest


def test_is_palindrome_corrected_spaces():
    assert is_palindrome_corrected("nbc c b n") == True
    
def test_is_palindrome_capitals():
    assert is_palindrome_corrected("hello oLLEH") == True
    
def test_is_palindrome_numbers():
    assert is_palindrome_corrected("hello 123 3 2 1 oll eh") == True
    
def test_is_palindrome_basic():
    assert is_palindrome_corrected(" 321 321") == False
    
def test_count_words_corrected_basic():
    assert count_words_corrected("hello my dearest, person")=={"hello" : 1, "my":1,"dearest,":1,  "person":1}

def test_second_largest_corrected():
    assert second_largest_corrected([1,3,4,5,6,6,7,7,8,8,8,9,9,9,1,1,0,0,1,1,2,2])==8



    