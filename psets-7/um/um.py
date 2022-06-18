import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    regex = re.compile(r'\b\W*um\W*', re.IGNORECASE)
    count = regex.findall(s)
    return len(count)

if __name__ == "__main__":
    main()
