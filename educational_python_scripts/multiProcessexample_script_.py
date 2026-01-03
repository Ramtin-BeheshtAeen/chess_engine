import os
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import time
import sys
import numpy as np
from multiprocessing import Pool
import time
from tqdm import tqdm
import h5py
import logging



logging.basicConfig(filename='worker.log', level=logging.INFO)

# Worker: processes one file, returns ONE array (can be big)
def process_file(path):
    results = []
    print(results)
    with open(path) as f:
        for line in f:
            x = int(line.strip())
            results.append(x * x)
    return results

# Main
#if __name__ == "__main__":
    # # Open a file in write mode
    # with open('./test_data/a.txt', 'w') as file:
    # # Write numbers from 1 to 100
    #     for number in range(1, 1000):
    #         file.write(f"{number}\n")


    # files = ["./test_data/a.txt", "./test_data/b.txt", "./test_data/c.txt", "./test_data/d.txt"]

    # start= time.time()
    # results = []
    # for file in files:
    #     with open (file) as f:
    #         for line in f:
    #             x = int(line.strip()) 
    #             results.append(x * x * x)
    # with open("output.txt", "w") as out:
    #     for file_results in results:
    #         out.write(f"{file_results}\n")
 
    # end = time.time()
    # print("Normal processing time:", end - start, "seconds")

    # start= time.time()
    # # Use one worker per file
    # processes = min(len(files), os.cpu_count())

    # with Pool(processes=processes) as pool:
    #     # pool.map returns a list of results per file
    #     results = pool.map(process_file, files)
    #     #logging.info(f"results in pool {results}")

    # # Write all results to disk without keeping everything in RAM at once
    # with open("output.txt", "w") as out:
    #     for file_results in results:
    #         for val in file_results:
    #             #logging.info(f"val {val}")
    #             out.write(f"{val}\n")
    # end = time.time()
    # print("Multiprocessing time:", end - start, "seconds")

    # print("Finished")

#it didnt have enough workload so it was not faster:
# Normal processing time: 0.006903886795043945 seconds
# Multiprocessing time: 1.358764886856079 seconds
# Finished

"""Logfile Output:
```
INFO:root:results in pool [[1, 4, 9, 16], [25, 36, 49, 64]]
INFO:root:val 1
INFO:root:val 4
INFO:root:val 9
INFO:root:val 16
INFO:root:val 25
INFO:root:val 36
INFO:root:val 49
INFO:root:val 64
```
"""

# Heavy CPU-bound work
def heavy_compute(x):
    acc = 0
    for i in range(50_000):   # <-- THIS is the workload
        acc += (x * i) % 97
    return acc

def process_file(path):
    results = []
    with open(path) as f:
        for line in f:
            x = int(line.strip())
            results.append(heavy_compute(x))
    return results


if __name__ == "__main__":

    files = [
        "./test_data/a.txt",
        "./test_data/b.txt",
        "./test_data/c.txt",
        "./test_data/d.txt",
    ]

    # -------- SINGLE PROCESS --------
    start = time.time()

    results = []
    for file in files:
        with open(file) as f:
            for line in f:
                x = int(line.strip())
                results.append(heavy_compute(x))

    with open("output_single.txt", "w") as out:
        for val in results:
            out.write(f"{val}\n")

    end = time.time()
    print("Normal processing time:", end - start, "seconds")

    # -------- MULTIPROCESSING --------
    start = time.time()

    processes = min(len(files), os.cpu_count())

    with Pool(processes=processes) as pool:
        results = pool.map(process_file, files)

    with open("output_multi.txt", "w") as out:
        for file_results in results:
            for val in file_results:
                out.write(f"{val}\n")

    end = time.time()
    print("Multiprocessing time:", end - start, "seconds")

    print("Finished")

#Normal processing time: 21.319135904312134 seconds
#Multiprocessing time: 15.18324875831604 seconds
