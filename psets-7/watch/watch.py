import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = re.compile(r'https?://(?:www.)?youtube.com/embed/(.+?)"')
    matched = pattern.search(s)
    if matched:
        result = f"https://youtu.be/{matched.group(1)}"
        return result

    else:
        return None

if __name__ == "__main__":
    main()
