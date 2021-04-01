# -*- coding: utf-8 -*-

import random
import time

from numba import njit, jit


@jit(nopython=True)
def pi_monte_carlo(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


if __name__ == '__main__':
    start_time = time.time()
    pi = pi_monte_carlo(10000000)
    end_time = time.time()
    print(pi)
    print(end_time - start_time)

'''
without numba, n=100_000_000
3.14158552
24.074887990951538

with numba, n=100_000_000
3.14156292
1.3931238651275635



without numba, n=10_000_000
3.1409692
2.663618803024292

with numba, n=10_000_000
3.1418056
0.5587382316589355
'''
