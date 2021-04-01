# -*- coding: utf-8 -*-

import multiprocessing


def worker_function(idx):
    # 在这里执行 CPU 密集型任务
    print(f'-> {idx + 1}')
    for i in range(30_000_000):
        pass
    print(f': {idx + 1}')


if __name__ == "__main__":
    num_processes = multiprocessing.cpu_count()
    print(f'cpu count: {num_processes}')
    num_processes = min(num_processes, 6)
    print(num_processes)
    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.map(worker_function, range(num_processes))
    pool.close()
    pool.join()
