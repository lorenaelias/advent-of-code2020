with open('day3.data') as f:
    lines = [y for y in f]
    height = len(lines)
    width = len(lines[0])
    lines = [list(line.rstrip()) for line in lines]
    
    trees = 0
    j = 0

    for l in range(len(lines)):
        if j > len(lines[l]) - 1:
            j = j % len(lines[l])
        if(lines[l][j] == "#"):
            trees += 1
        j += 3

    print(trees, "trees in the way.")