from seasons import check

def test_seasons():
  assert check('1997-12-10') == ('1997', '12', '10')
  assert check('19999-12-10') == None
  assert check('Oct 1, 12') == None