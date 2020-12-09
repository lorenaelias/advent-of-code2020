with open('day2.data') as f:
    lines = [[x[0].split('-'), x[1][0], x[2]] for x in [y.split() for y in f]]
    
    # first half
    answer1 = [True if l[2].count(l[1]) >= int(l[0][0]) and l[2].count(l[1]) <= int(l[0][1]) else False for l in lines]
    print("valid passwords = ", sum(answer1))

    # last half
    answer2 = [  ( l[2][ int(l[0][0])-1 ] == l[1] ) ^ ( l[2][ int(l[0][1])-1 ] == l[1] ) for l in lines]
    print("valid passwords = ", sum(answer2))