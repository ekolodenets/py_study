import functools
import time


def elapsed_time(f):
    start = time.time()
    result = f()
    finish = time.time()
    return result, finish - start


def fib1(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib1(n - 2) + fib1(n - 1)


@functools.lru_cache(maxsize=None)
def fib2(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib2(n - 2) + fib2(n - 1)


for n in range(1, 100):
    # f1, t1 = elapsed_time(lambda: fib1(n))
    f2, t2 = elapsed_time(lambda: fib2(n))
    # assert f1 == f2
    print(f' {t2:.3f} fib({n:2}) = {f2}')