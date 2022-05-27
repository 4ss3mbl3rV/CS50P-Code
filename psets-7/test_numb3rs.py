from numb3rs import validate
import pytest

def test_numb3rs():
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False
    assert validate('192.168.100.1') == True
