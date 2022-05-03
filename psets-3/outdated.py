months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
delimiter = ['/', ' ']

while True:
    userIn = input('Date: ')
    if '/' in userIn:
        month, date, year = userIn.split(delimiter[0])
        if month.isdigit():
            if int(date) <= 31 and int(month) <= 12:
                print(f'{int(year)}-{int(month):02}-{int(date):02}')
                break
        else:
            continue
    elif ' ' in userIn:
        month, date, year = userIn.split(delimiter[1])
        date = date.replace(',', '')
        if date.isdigit():
            if int(date) <= 31:
                if month.capitalize() in months:
                    month = months.index(month) + 1
                    print(f'{int(year)}-{int(month):02}-{int(date):02}')
                    break
        else:
            continue
