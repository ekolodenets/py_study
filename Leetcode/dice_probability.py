import itertools


def rolldice_sum_prob(sum_, dice_amount):
    if sum_ > dice_amount * 6:
        return 0
    t = [[1, 2, 3, 4, 5, 6] for _ in range(dice_amount)]
    l = list(itertools.product(*t)) # list of all possible combinations
    times = 0
    for i in l:
        if sum(i) == sum_:
            times += 1

    return times / (6 ** dice_amount)




print(rolldice_sum_prob(11, 2))
assert rolldice_sum_prob(11, 2) == 0.055555555555
assert rolldice_sum_prob(8, 2) == 0.13888888889
assert rolldice_sum_prob(8, 3) == 0.0972222222222