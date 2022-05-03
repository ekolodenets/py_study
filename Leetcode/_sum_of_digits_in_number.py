def func(num: int) -> int:
    '''input number & return sum on digits'''
    x = sum(map(int, str(num)))
    return x if x < 10 else func(x)

print(func(567))