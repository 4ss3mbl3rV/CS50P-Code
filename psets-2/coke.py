def main():
    left = True
    accepted_coin = [25,10,5]
    cost = 50
    while left:
        print(f'Amount Due: {cost}')
        userIn = int(input('Insert Coin: '))
        if userIn in accepted_coin:
            if cost == 0:
                print(f'Change Owed: {cost}')
                left = False
            elif cost >= userIn:
                cost -= userIn

if __name__ == '__main__':
    main()
