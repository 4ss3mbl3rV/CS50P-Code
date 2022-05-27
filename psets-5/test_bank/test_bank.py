from bank import value

def test_return_zero():
    assert value('hello John') == 0
    assert value('Hello') == 0
    assert value('HeLlO, John') == 0

def test_return_twenties():
    assert value('Howdy') == 20
    assert value('hi') == 20

def test_return_onehundred():
    assert value('What\'s up?') == 100
    assert value('Good to see you') == 100
