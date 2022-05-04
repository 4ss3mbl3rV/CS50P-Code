import requests, sys

try:
  api = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  json = api.json()
  if len(sys.argv) == 1 and len(sys.argv) <= 2:
    print('Missing command-line argument')
    sys.exit(1)
  else:
    if not float(sys.argv[1]):
      print('Command-line argument is not a number')
    else:
      currency = json['bpi']['USD']['rate_float'] * float(sys.argv[1])
      print(f'${currency:,.4f}')
except requests.RequestException:
  sys.exit(1)