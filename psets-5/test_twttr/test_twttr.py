from twttr import shorten

def test_twttr():
  assert shorten('Twitter') == 'Twttr'
  assert shorten('PYTHON') == 'PYTHN'
  assert shorten('CS50P') == 'CS50P'
  assert shorten('What\'s are you doing?') == 'Wht\'s r y dng?'
  assert shorten('What\'s going on?') == 'Wht\'s gng n?'