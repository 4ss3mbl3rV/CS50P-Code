import random


def main():
    attempts = 3
    amount = 10
    score = 0
    level = get_level()
    while amount != 0:
      x, y = generate_integer(level)
      while attempts > 0:
        answer = int(input(f'{x} + {y} = '))
        if answer == eval(f'{x} + {y}'):
          amount -= 1
          score += 1
          break
        else:
          print('EEE')
          attempts -=1
      if attempts == 0:
        print(f'{x} + {y} = {int(x) + int(y)}')
        attempts = 3
        amount -= 1
    print(f'Score: {score}')


def get_level():
    while True:
      level = int(input('Level: '))
      if level not in [1,2,3]:
        continue
      else:
        return level


def generate_integer(level):
  lower = int(level != 1) * 10 ** (level-1)
  x = random.randint(lower, 10 ** level)
  y = random.randint(lower, 10 ** level)
  return x, y


if __name__ == "__main__":
    main()