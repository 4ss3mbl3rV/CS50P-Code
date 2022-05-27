import csv
from sys import exit, argv
def main():
    if len(argv) <= 1:
        print('Too few command-line arguments')
        exit(1)
    elif len(argv) > 3:
        print('Too many command-line arguments')
        exit(1)
    else:
        read = csvReader(argv[1])
        generateCSV(argv[2], read)

def csvReader(data):
    datasets = []
    try:
        with open(data, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in spamreader:
                datasets.append(row)
        return datasets
    except FileNotFoundError:
        print('Could not read {}'.format(data))
        exit(1)

def generateCSV(filename, data):
    with open(filename,'w', newline='') as csvfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in range(len(data)):
            if row == 0:
                continue
            else:
                fullname = data[row][0].split(',')
                firstname = fullname[1].strip()
                lastname = fullname[0].strip()
                writer.writerow({'first': firstname, 'last': lastname, 'house': data[row][1]})
    return 0
if __name__ == '__main__':
    main()