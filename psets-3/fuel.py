while True:
    try:
        userIn = input('Fraction: ').strip().split('/')
        if userIn[0].isdigit() and userIn[1].isdigit() and int(userIn[0]) <= int(userIn[1]):
            result = eval(f'{userIn[0]} / {userIn[1]}')
            if result <= 0.1:
                print('E')
                break
            elif 0.9 <= result <= 1:
                print('F')
                break
            else:
                print(f'{int(result * 100)}%')
                break
        else:
            continue
    except (ValueError, ZeroDivisionError):
        continue
