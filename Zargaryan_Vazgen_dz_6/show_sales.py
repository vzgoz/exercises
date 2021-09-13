import sys

with open('bakery.csv', 'r',encoding='utf-8') as f:
    if len(sys.argv) == 1:
        for line in f:
            print(line,end= '')

    if len(sys.argv) == 2:
        n = 1
        for line in f:
            if n >= int(sys.argv[1]):
                print(line,end='')
            n += 1
        if len(sys.argv) == 3:
            n = 1
            for line in f:
                if n >= int(sys.argv[1]) and n <= int(sys.argv[2]):
                    print(line,end='')
                n += 1