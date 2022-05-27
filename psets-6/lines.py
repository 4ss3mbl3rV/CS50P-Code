#! python3
#! /usr/bin/python3

from sys import argv, exit

def main():
    count = 0
    if len(argv) != 2:
        print('Too few command-line arguments')
        exit(1)
    elif len(argv) > 2:
        print('Too many command-line arguments')
        exit(1)
    elif not argv[1].endswith('.py'):
        print('Not a Python file')
        exit(1)
    else:
        try:
            with open(f'{argv[1]}', 'r') as file:
                text = file.readlines()
                text = [x.lstrip() for x in text]
            for line in text:
                if line.startswith('#'):
                    continue
                elif line == '':
                    continue
                else:
                    count +=1
            print(count)
        except FileNotFoundError:
            print('File does not exist')
            exit(1)

if __name__ == '__main__':
    main()
