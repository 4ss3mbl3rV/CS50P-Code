from tkinter import font
from pyfiglet import Figlet
from random import choice
import sys

def main():
  figlet = Figlet()
  fonts = figlet.getFonts()
  if len(sys.argv) >= 2 and len(sys.argv) <= 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fonts:
            userIn = input('Input: ')
            f = sys.argv[2]
            figlet.setFont(font=f)
            print(figlet.renderText(userIn))
        else:
            sys.exit(1)
    else:
      sys.exit(1)
  else:
    userIn = input('Input: ')
    f = choice(fonts)
    figlet.setFont(font=f)
    print(figlet.renderText(userIn))


if __name__ == '__main__':
  main()