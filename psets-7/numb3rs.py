import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
    if regex.match(ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
