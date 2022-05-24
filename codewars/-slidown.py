# * With the input `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`
# * Your function should return `23`.

import itertools
def longest_slide_down(arr):
    """
    Slide down the array and return the max sum of the numbers
    """
    # Variant 1 out of memory
    # combinations = [p for p in itertools.product(*arr)]
    # sums = []
    # for combination in combinations:
    #     t = []
    #     [t.append((combination[i], arr[i].index(combination[i]))) for i in range(len(combination))]
    #     g = [t[0][0]]
    #
    #     # for i in range(1, len(t)):
    #     #     if t[i-1][1] == t[i][1] or t[i-1][1]+1 == t[i][1]:
    #     #         g.append(t[i][0])
    #     #     else:
    #     #         g = []
    #
    #     [g.append(t[i][0]) if t[i - 1][1] == t[i][1] or t[i - 1][1] + 1 == t[i][1] else g.clear() for i in range(1, len(t))]
    #     if len(g) == len(arr):
    #         print(g)
    #     sums.append(sum(g)) if len(g) == len(arr) else []
    # # print(sums)
    # return max(sums)

    # Variant
    if len(arr) == 1:
        return arr[0][0]
    else:
        t = []
        for i in range(1, len(arr)-1):
            a = [arr[0]]
            b = [arr[0]]
            for s in range(len(arr[i])):
                a.append([arr[i][s],arr[i+1][s]])
                b.append(arr[i+1][s])
                print(arr[i][s], (arr[i+1][s], arr[i+1][s+1]), arr[i][s]+arr[i+1][s], arr[i][s]+arr[i+1][s+1])
                print(a, b)

def lst(lst):
    pass










# print(longest_slide_down([
#             [75],
#             [95, 64],
#             [17, 47, 82],
#             [18, 35, 87, 10],
#             [20,  4, 82, 47, 65],
            # [19,  1, 23, 75,  3, 34],
            # [88,  2, 77, 73,  7, 63, 67],
            # [99, 65,  4, 28,  6, 16, 70, 92],
            # [41, 41, 26, 56, 83, 40, 80, 70, 33],
            # [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            # [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            # [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            # [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            # [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            # [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            # ]))
# print(longest_slide_down([[3], [7, 4], [2, 4, 6]]))
# print(longest_slide_down([[3], [7, 4]])),
# print(longest_slide_down([[3], [7, 4], [2, 4, 6]]))
print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))


# assert longest_slide_down([[3], [7, 4]]) == 10
# assert longest_slide_down([[3], [7, 4], [2, 4, 6]]) == 14
# assert longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) == 23
# assert longest_slide_down([
#             [75],
#             [95, 64],
#             [17, 47, 82],
#             [18, 35, 87, 10],
#             [20,  4, 82, 47, 65],
#             [19,  1, 23, 75,  3, 34],
#             [88,  2, 77, 73,  7, 63, 67],
#             [99, 65,  4, 28,  6, 16, 70, 92],
#             [41, 41, 26, 56, 83, 40, 80, 70, 33],
#             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#             [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#             [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#             [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#             [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#             [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
#             ]) == 1074