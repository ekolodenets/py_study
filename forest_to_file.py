"""
                             *
                            ***
                             *
                            ***
                           *****
                             *
                   *        ***
                  ***      *****
                   *      *******
                  ***        *
                 *****      ***
           *       *       *****
          ***     ***     *******
           *     *****   *********
          ***   *******      *
     *   *****     *        ***
    ***    *      ***      *****
     *    ***    *****    *******
 *  ***  *****  *******  *********  *
**************************************

"""


def plant_forest(*args):
    forest = []
    max_level_amount = sum([x+2 for x in range(max(args))])
    for n in args:
        width = n * 2 + 1
        current_lvl = sum([j + 2 for j in range(n)])
        tree = [' '*width for _ in range(max_level_amount - current_lvl)]
        level = [f'{" "*int((width-1)/2)}*{" "*int((width-1)/2)}',
                 f'{" "*int((width-3)/2)}***{" "*int((width-3)/2)}']

        tree.extend(level)
        for i in range(1, n):
            lvl = '***' + "**" * i
            level.append(" " * int((width - len(lvl))/2) + lvl + ' '*int((width - len(lvl))/2))
            tree.extend(level)
        forest.append(tree)

    with open('forest.txt', 'w') as f:
        for col in range(max_level_amount):
            for row in range(len(forest)):
                f.write(forest[row][col])
            f.write('\n')



plant_forest(1, 2, 3, 4, 5, 1)
