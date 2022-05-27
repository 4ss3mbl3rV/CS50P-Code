vowels = ['A', 'E', 'I', 'O', 'U']
def main():
  userIn = input('Input: ')
  print('Output:', shorten(userIn))
def shorten(word):
  newWord = ''
  for w in word:
    if w.upper() in vowels:
      continue
    else:
      newWord += w
  return newWord

if __name__ == '__main__':
  main()