TOTAL = {}
count = 1
while True:
    try:
        item = input()
        if len(TOTAL) == 0:
            TOTAL.setdefault(item.upper(), count)
        else:
            if item.upper() in TOTAL.keys():
                count +=1
                TOTAL[item.upper()] = count
            else:
                count = 1
                TOTAL.setdefault(item.upper(), count)
                
    except EOFError:
        for key, value in sorted(TOTAL.items()):
            print(f'{value} {key}')
        break
