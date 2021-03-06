'''
Nesting Structure Comparison

Complete the function/method (depending on the language) to return true/True when its argument is an array that
has the same nesting structures and same corresponding length of nested arrays as the first array.
For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

'''


def same_structure_as(original, other):
    one = []
    two = []
    return unzip(original, one) == unzip(other, two) if type(original) == type(other) else False

def unzip(l,temp):
    for i in l:
        if isinstance(i, list) and len(i) > 0:
            temp.append(1)
            unzip(i, temp)
            temp.append(1)
        if isinstance(i, int) or isinstance(i, str):
            temp.append(2)
        else:
            temp.append(0)
    return temp


# print(same_structure_as([[[],[]]], [[1,1]]))
# print(same_structure_as([1, 1, 1], [2, 2, 2]))
# print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
# print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
# print(same_structure_as([], {}))
# print(same_structure_as([-5, [[-1, -11], [[-10, 20, 11, 1], [[17, -1], 18, [-6, -14, -18, [-16, -10, -7, -19]], [13, [5, 10]]], [[12, -8], 19], -16], [12, -12], 9], [1, [[[[-14, [[[-19, -1, [[[[], 7], [[[15, [1, [[-17, -4, 8, 2], 11, 14, [-6, [9, -7], -6, [18, [[-7, -18], 18, [-13, 11], [[5, 12], 2]], 18, 20]]], [[-19, -20], -20, 1, 6], [-13, -16, 6, -4]], [-15, [8, 19, [], 13], [9, 3], 19], -7], -10], -12, 14, 3], [-16, 11], -4], 3], [7, [17, 9, [], 17]]], [[18, [[[-3, 18], -13], [-15, -13, -12, 4]]], -10]], [-11, -3, -8, 8], [], 19]], -9], 6], -5, [[3, -10], -10, [-15, -19, [-14, -8], 10], -6], -9], [10, -20], -1], 6, [-10, -13, -14, 11], -7, 13, [], 17, 19, 18, [-9, -3], [19, -9, 8, [17, -9]], -19, -7, -16, -18, [11, 8, [-13, -12], -10], -10, 5, 20, [[[16, [-7, -6], 12, 18], -8], [], -20, [15, -4, [-4, -17, -5, [[4, [[[[-4, -15, 10, -20], 12], [-20, -2, [[[-17, -2, -19, 16], 18, 3, [-19, [-2, 19, -6, 12], 3, -6]], -11], -6]], 12, 10, -7]], [[12, -18], [], [-8, 18], [-12, 6]]]], -14]]], [6, [[0, 20], [[10, -1, -9, -18], [[6, -9], -16, [3, -17, 6, [2, -3, 15, -2]], [-15, [-16, 19]]], [[19, 20], 4], 2], [-6, -5], -10], [2, [[[[10, [[[6, -5, [[[[], 14], [[[8, [9, [[20, -17, 12, -5], 18, -14, [13, [-18, 2], 1, [-7, [[-18, -19], -7, [7, -12], [[-1, -10], 2]], 1, -10]]], [[16, -4], 12, 18, 1], [4, -15, -5, -9]], [-20, [-18, -20, [], 20], [14, -9], 7], -11], -2], 7, 18, -13], [-12, -10], 17], 15], [-11, [1, -7, [], 17]]], [[20, [[[-8, 15], 18], [8, 15, -11, -11]]], -19]], [-17, 8, 9, 2], [], -15]], -11], -17], 17, [[16, -5], -1, [-13, 20, [12, -18], 19], 13], -2], [-6, -9], 9], 3, [-12, -18, 17, -1], -7, -17, [], -13, -9, -12, [0, -9], [-7, -10, 8, [5, -4]], -7, 11, 1, -16, [6, -14, [17, 9], -5], 14, -17, -19, [[[-20, [5, 12], 9, -2], 3], [], -15, [-20, 15, [-20, -7, -2, [[13, [[[[-10, -1, 8, -2], 12], [-2, -4, [[[-6, 14, 9, 1], 8, -14, [-8, [-20, 14, 5, 11], 15, -8]], -7], -4]], -14, -11, 17]], [[-12, 7], [], [1, -16], [11, -9]]]], 12]]]))


# assert (same_structure_as([-1, 10, [-14, 20], [5, 17, 9, 19], -10, -1, -1, -15, -17, 2, [-2, [-15, -10], 16, -3], -2, [[], -7], [[-12, -19, [[[8, -8], [-13, -19, 4, -17], [10, [1, 19], -11, 2], 8], 14], -8], 6, [-11, -5, -19, 13], 2]], [9, -18, [-18, -1], [-19, -14, -18, 13], 14, -16, 18, -15, -18, 3, [-10, [19, 18], 0, 19], -18, [[], -13], [[-13, -16, [[[-13, 20], [15, 8, 4, -5], [10, [3, 5], 6, -15], 0], -9], -12], 4, [8, 19, 10, -9], -20]]) == True)
# assert (same_structure_as([18, -11, 4, [18, [-5, 9]], -18, -20, [-7, -9], -12, -4, 19, -16, [14, [[15, 8, -18, [2, [[-2, [19, -2, -15, -8], -20, 13], -6, 11, -2], [19, -19, 4, -7], [3, [[-20, [[-4, 11], []]], 15], [7, [-7, -15, 7, 6]], [-16, -19]]]], -8]], -7, 1, 17, -5, -10, [-2, -5, 13, [2, -5, 1, [-1, 4, 8, -17]]], -10, [16, 14, [-16, 1, 17, -14], [[[12, 7, 12, [-17, [14, 14]]], -18, [[-18, -14], -15], [[6, [-5, -8, 2, 9]], 9]], -4]]], [-17, -19, 14, [13, [-5, 2]], 20, 5, [7, 11], 1, 7, 17, -2, [18, [[-4, -18, -13, [-5, [[-20, [-14, -17, 9, 14], 9, 13], -19, 13, -9], [-16, 16, 5, 3], [14, [[0, [[-4, -17], []]], -4], [14, [-17, -18, 1, 2]], [8, -17]]]], 8]], -10, 6, 4, -13, -13, [-13, -9, -16, [16, -9, -10, [17, 4, -18, 8]]], -14, [19, 5, [-5, 13, 9, 0], [[[16, 16, 8, [-9, [-4, 2]]], -15, [[3, -7], -18], [[8, [-13, -15, 20, 8]], -17]], -11]]]) == True)
# assert (same_structure_as([[], -8, 3, [-14, 2], -20, -16, 19, 19, -7, -2, -1, -15, -3, 17, 2, 11, -9, -16, -9, -4, [1, 19, 12, -9], 1, [-18, [-16, 16]], -5, -4, -2, -6, [13, [12, 12]], [16, [-10, -5]], -10, 7, 7, [-5, -5], 11], [[], -18, -10, [4, -17], 13, -18, -13, -16, -17, -12, -3, -2, 14, -9, -11, 9, 20, -10, 9, 19, [-3, -1, 5, 12], 1, [14, [5, 0]], 7, 15, -17, 0, [20, [-5, -18]], [7, [14, -20]], -11, -1, -9, [14, 3], 10]) == True)
# assert (same_structure_as([1, [1, 1]], [2, [2, 2]]) == True)
# assert (same_structure_as([1, [1, 1]], [2, [2, 2]]) == True)

# assert (same_structure_as([1, [1, 1]], [2, [2, 2]]) == True)
# assert (same_structure_as([1, [1, 1]], [2, [2, [2, 2]]]) == False)
# assert (same_structure_as([1, [1, 1]], [[2, 2], 2]) == False)
# assert (same_structure_as([-5, [[-1, -11], [[-10, 20, 11, 1], [[17, -1], 18, [-6, -14, -18, [-16, -10, -7, -19]], [13, [5, 10]]], [[12, -8], 19], -16], [12, -12], 9], [1, [[[[-14, [[[-19, -1, [[[[], 7], [[[15, [1, [[-17, -4, 8, 2], 11, 14, [-6, [9, -7], -6, [18, [[-7, -18], 18, [-13, 11], [[5, 12], 2]], 18, 20]]], [[-19, -20], -20, 1, 6], [-13, -16, 6, -4]], [-15, [8, 19, [], 13], [9, 3], 19], -7], -10], -12, 14, 3], [-16, 11], -4], 3], [7, [17, 9, [], 17]]], [[18, [[[-3, 18], -13], [-15, -13, -12, 4]]], -10]], [-11, -3, -8, 8], [], 19]], -9], 6], -5, [[3, -10], -10, [-15, -19, [-14, -8], 10], -6], -9], [10, -20], -1], 6, [-10, -13, -14, 11], -7, 13, [], 17, 19, 18, [-9, -3], [19, -9, 8, [17, -9]], -19, -7, -16, -18, [11, 8, [-13, -12], -10], -10, 5, 20, [[[16, [-7, -6], 12, 18], -8], [], -20, [15, -4, [-4, -17, -5, [[4, [[[[-4, -15, 10, -20], 12], [-20, -2, [[[-17, -2, -19, 16], 18, 3, [-19, [-2, 19, -6, 12], 3, -6]], -11], -6]], 12, 10, -7]], [[12, -18], [], [-8, 18], [-12, 6]]]], -14]]], [6, [[0, 20], [[10, -1, -9, -18], [[6, -9], -16, [3, -17, 6, [2, -3, 15, -2]], [-15, [-16, 19]]], [[19, 20], 4], 2], [-6, -5], -10], [2, [[[[10, [[[6, -5, [[[[], 14], [[[8, [9, [[20, -17, 12, -5], 18, -14, [13, [-18, 2], 1, [-7, [[-18, -19], -7, [7, -12], [[-1, -10], 2]], 1, -10]]], [[16, -4], 12, 18, 1], [4, -15, -5, -9]], [-20, [-18, -20, [], 20], [14, -9], 7], -11], -2], 7, 18, -13], [-12, -10], 17], 15], [-11, [1, -7, [], 17]]], [[20, [[[-8, 15], 18], [8, 15, -11, -11]]], -19]], [-17, 8, 9, 2], [], -15]], -11], -17], 17, [[16, -5], -1, [-13, 20, [12, -18], 19], 13], -2], [-6, -9], 9], 3, [-12, -18, 17, -1], -7, -17, [], -13, -9, -12, [0, -9], [-7, -10, 8, [5, -4]], -7, 11, 1, -16, [6, -14, [17, 9], -5], 14, -17, -19, [[[-20, [5, 12], 9, -2], 3], [], -15, [-20, 15, [-20, -7, -2, [[13, [[[[-10, -1, 8, -2], 12], [-2, -4, [[[-6, 14, 9, 1], 8, -14, [-8, [-20, 14, 5, 11], 15, -8]], -7], -4]], -14, -11, 17]], [[-12, 7], [], [1, -16], [11, -9]]]], 12]]]) == True)
# assert (same_structure_as([12, 16, 20, [13, -1], -14, 8], [-2, -11, 11, [6, -13], -8, -13]) == True)
# assert (same_structure_as([-20, -6, -4, 16, -16, -14], [-13, 5, 3, -6, -7, -11]) == True)
# assert (same_structure_as([1, '[', ']'], ['[', ']', 1]) == True)
