from psets-2 import plates.is_valid

def test_plates():
    assert is_valid('CS50P') == False
    assert is_valid('CS05') == False
    assert is_valid('CS50') == True
    assert is_valid('1234') == False
    assert is_valid('NRVOUS') == True
    assert is_valid('H') == False
    assert is_valid('') == False
    assert is_valid('OUT TIME') == False
    assert is_valid('OUTATIME') == False
    assert is_valid('PI3.14') == False