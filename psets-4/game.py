import random

answer = 0
guess = 0
state = True
while state:
  try:
    level = int(input('Level: ').strip())
    answer = random.randint(1, level)
    while guess != answer:
      guess = int(input('Guess: ').strip())
      if guess < answer:
        print('Too small!')
      elif guess == answer:
        print('Just right!')
        state = False
      else:
        print('Too large!')
  except ValueError:
    continue