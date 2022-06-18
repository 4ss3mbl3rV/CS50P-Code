from response import validator_checker

def test_response():
    assert validator_checker("malan@harvard.edu") == "Valid"
    assert validator_checker("justincase@wearehackerone.com") == "Valid"
    assert validator_checker("malan@@@harvard.edu") == "Invalid"
    assert validator_checker("justincase@wearehackerone..com") == "Invalid"
