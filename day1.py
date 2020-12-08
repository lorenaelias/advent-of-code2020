import itertools

with open('day1.data') as f:
    list = [int(x) for x in f]
    uniquelist = set(list)

    # parte 1
    for n in itertools.combinations(uniquelist, 2):
        if n[0] + n[1] == 2020:
            print(n[0], ' + ', n[1], ' = 2020')
            print(n[0], ' * ', n[1], ' = ', n[0]*n[1])

    # parte 1
    for n in itertools.combinations(uniquelist, 3):
        if n[0] + n[1] + n[2] == 2020:
            print(n[0], ' + ', n[1], '+', n[2],' = 2020')
            print(n[0], ' * ', n[1], '*', n[2],' = ', n[0]*n[1]*n[2])