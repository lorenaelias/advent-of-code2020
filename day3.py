def trees_from_slope(slope):
    i = 0
    j = 0
    trees = 0
    while i < len(lines):
        if j > len(lines[i]) - 1:
            j = j % len(lines[i])
        if(lines[i][j] == "#"):
            trees += 1
        j += slope[0]
        i += slope[1]
    return trees

with open('day3.data') as f:
    lines = [y for y in f]
    height = len(lines)
    width = len(lines[0])
    lines = [list(line.rstrip()) for line in lines]
    all_trees = 1
    
    trees = trees_from_slope([3, 1])

    print(trees, "trees in the way.\n\n")

    # last part
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    for slope in slopes:
        actual_trees = trees_from_slope(slope)
        print(actual_trees, "trees in the way.")
        all_trees *= actual_trees
    print("Product: ", all_trees)