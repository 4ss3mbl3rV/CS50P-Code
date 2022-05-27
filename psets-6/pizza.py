import csv
from sys import argv, exit
from tabulate import tabulate

def main():
    if len(argv) != 2:
        print('Too few command-line arguments')
        exit(1)
    elif len(argv) > 2:
        print('Too many command-line arguments')
        exit(1)
    elif not argv[1].endswith('.csv'):
        print('Not a CSV file')
        exit(1)
    else:
        convert(argv[1])
    print(tabulate(tables, header, tablefmt='grid'))

def convert(data):
    global header
    global tables
    with open(f'{argv[1]}', newline="") as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        reader = [row for row in reader]
    for i in range(len(reader)):
        if i == 0:
            header = reader[i]
        else:
            tables.append(reader[i])
if __name__ == '__main__':
    header = []
    tables = []
    main()
