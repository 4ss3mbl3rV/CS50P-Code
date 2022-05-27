from fuel import convert, gauge
import pytest

def test_ZeroDivisionErr():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
def test_ValueErr():
    with pytest.raises(ValueError):
        convert('dog/cat')

def test_return_percentage():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'
