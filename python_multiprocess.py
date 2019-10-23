"""Notes
Pool object which offers a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes (data parallelism).
```
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
```

Data Parallelism
"""

from time import time
import multiprocessing as mp
import numpy as np
from tqdm import tqdm

################################################################################
# Process class

# processes = [mp.Process(target=core, args=(1000,100)) for x in range(4)]
#
# # Run processes
# for p in processes:
#     p.start()
#
# # Exit the completed processes
# for p in processes:
#     p.join()


################################################################################
# Pool class
# aa = [1000]
# a = [1000, 100]
# p = mp.Pool(processes=4)
# # function takes only single argument
# p.map(core, aa * 4)
# # function takes multiple arguments
# p.starmap(core, [a] * 4)


def core(pid: int, return_dict: dict, n=1000, m=100):
    start = time()
    for i in tqdm(range(n), unit=" loan", desc=f"Process {pid}", position=pid):
        a = np.arange(n)
        np.random.choice(a, m)
    return time() - start


def multi_core_execution(num_of_proc: int, n_list: list):
    """"""
    manager = mp.Manager()
    return_dict = manager.dict()
    p = mp.Pool(processes=num_of_proc)
    arg_list = [(pid, return_dict, n) for pid, n in enumerate(n_list)]
    result = p.starmap(core, arg_list)

    return result


################################################################################
# subprocess communication
# As we are communicating outside python environment, we need to serialize all
#    data and utilize stdin/stdout
################################################################################
# main function file
import subprocess
import pickle
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random((5, 5)))
p = subprocess.Popen(["python", "subp.py"], stdin=subprocess.PIPE)
p.communicate(pickle.dumps(df))

# sub function file `subp.py`
import sys
import pickle

df = pickle.loads(sys.stdin.buffer.read())
df.to_csv("yes.csv")


if __name__ == "__main__":
    return_dict = multi_core_execution(4, [130_000, 120_000, 110_000, 100_000])
