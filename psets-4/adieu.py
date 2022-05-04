import inflect

name = []
p = inflect.engine()
while True:
  try:
    userIn = input('Name: ')
    name.append(userIn)
  except EOFError:
    print(f'\nAdieu, adieu, to {p.join(name)}')
    break