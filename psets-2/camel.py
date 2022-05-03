def caseConvert(msg):
    newCase = ''
    for i in msg:
        if i.isupper():
            newCase += f'_{i.lower()}'
        else:
            newCase += i
    return newCase
def main():
    userIn = input('camelCase: ')
    print('snake_case: ' + caseConvert(userIn))

if __name__ == '__main__':
    main()
